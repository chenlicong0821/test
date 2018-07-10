import cjson
import json
import decimal

a = decimal.Decimal('5.5')

minDataStrDict = {'date':'20180709','data':[],'prec':a}
minDataJsonStr = json.dumps(minDataStrDict)

print minDataStrDict
print minDataJsonStr
