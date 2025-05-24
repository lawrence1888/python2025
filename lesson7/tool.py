def caculate_bmi(h:int,w:int)->float:
    return w / (h / 100) ** 2

def get_state(b:float)->str:
    if b < 18.5:
        return "體重過輕"
    elif b < 24:
        return "正常範圍"
    elif b < 27:
        return "過重"
    elif b < 30:
        return "輕度肥胖"
    elif b < 35:
        return "中度肥胖"
    else:
        return "重度肥胖"