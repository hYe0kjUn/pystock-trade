import win32com.client

def __request(endpoint):
    return win32com.client.Dispatch("CpUtil."+str(endpoint))

def GetLimitRemainCount():
    """
    호출 제한까지 남은 호출량 확인
    """
    
    res = __request('CpCyBos').GetLimitRemainCount("LT_NONTRADE_REQUEST")
    return res
  
print(GetLimitRemainCount())