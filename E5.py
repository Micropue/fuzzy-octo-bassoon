import time
# 初始化专注时间
focus_time = 25  # 以分钟为单位
# 开始专注
start_time = time.time()
while time.time() - start_time < focus_time * 60:
    # 显示时钟
    print(f"专注中...{focus_time - int((time.time() - start_time) / 60)}:00")
# 专注时间结束
print("专注时间结束！")
