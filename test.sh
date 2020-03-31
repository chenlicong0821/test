
//流出流量处理
iptables -t nat -N ISTIO_REDIRECT   //增加ISTIO_REDIRECT链处理流出流量
iptables -t nat -A ISTIO_REDIRECT -p tcp -j REDIRECT --to-port "${PROXY_PORT}" // 重定向流量到Sidecar的端口上
iptables -t nat -N ISTIO_OUTPUT // 增加ISTIO_OUTPUT链处理流出流量
iptables -t nat -A OUTPUT -p tcp -j ISTIO_OUTPUT// 将OUTPUT链的流量重定向到ISTIO_OUTPUT链上
for uid in ${PROXY_UID}; do
    iptables -t nat -A ISTIO_OUTPUT -m owner --uid-owner "${uid}" -j RETURN //Sidecar本身的流量不转发
done
for gid in ${PROXY_GID}; do
    iptables -t nat -A ISTIO_OUTPUT -m owner --gid-owner "${gid}" -j RETURN  //Sidecar本身的流量不转发
done
iptables -t nat -A ISTIO_OUTPUT -j ISTIO_REDIRECT //将ISTIO_OUTPUT链的流量转发到ISTIO_REDIRECT

//流入流量处理
iptables -t nat -N ISTIO_IN_REDIRECT  //增加ISTIO_IN_REDIRECT链处理流入流量
iptables -t nat -A ISTIO_IN_REDIRECT -p tcp -j REDIRECT --to-port "${PROXY_PORT}" // 将流入流量重定向到Sidecar端口
iptables -t ${table} -N ISTIO_INBOUND //增加ISTIO_INBOUND链处理流入流量
iptables -t ${table} -A PREROUTING -p tcp -j ISTIO_INBOUND //将PREROUTING的流量重定向到ISTIO_INBOUND链
iptables -t nat -A ISTIO_INBOUND -p tcp --dport "${port}" -j ISTIO_IN_REDIRECT //将ISTIO_INBOUND链上指定目的端口的流量重定向到ISTIO_IN_REDIRECT链