#include <iostream>
#include <string.h>

using namespace std;

#define BUY_SELL_NUM    10       /* number of buy or sell info   */

#define MAX_BROKER_QUEUE_COUNT  40   /*number of security broker queue info */

#define MAX_STOCK_CODE_LEN   12

typedef struct buySellInfo  /* info of buy and sell */
{
    int     price;
    float   order;
    float   volume;
} BUY_SELL_INFO;

/*港股行情数据*/
typedef struct rawHkQuotation
{

    char          code[MAX_STOCK_CODE_LEN];           /*港股代码*/
    float         tradePrice;        /*当前价*/
    float         nominalPrice;      /*按盘价*/

    float         bidPrice;          /*买入价*/
    float         askPrice;          /*卖出价*/

    float         highPrice;         /*最高价*/
    float         lowPrice;          /*最低价*/

    float         upperPrice;        /*CAS机制最高价*/
    float         lowerPrice;        /*CAS机制最低价*/

    float         todayOpen;         /*今日开盘价*/
    float         yestClose;         /*昨日收盘价*/

    double        turnOver; //万     /*总成交额*/
    double        tradeSize;         /*当前成交量*/
    double        totalSize;  //万   /*总成交量*/

    int           date;              /*当前日期*/
    int           time;              /*当前时间*/

    /* buy and sell */
    BUY_SELL_INFO buys[BUY_SELL_NUM];       /* buy infos    */
    BUY_SELL_INFO sells[BUY_SELL_NUM];      /* sell infos   */

    int           buySellSide;      //broker side
    int           brokerQueueBuy[MAX_BROKER_QUEUE_COUNT];
    int           brokerQueueSell[MAX_BROKER_QUEUE_COUNT];
}RAW_HK_QUOTATION;

int main(int argc, char const *argv[])
{
    RAW_HK_QUOTATION a;
    memset(&a, 0, sizeof(a));

    cout << sizeof(a) << endl;
    cout << sizeof(a.buys) << endl;
    cout << sizeof(a.brokerQueueSell) << endl;

    cout << a.tradePrice << endl;
    cout << a.turnOver << endl;

    return 0;
}
