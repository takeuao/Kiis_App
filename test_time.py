import datetime

now = datetime.datetime.now()
print(f"今は: {now}")

target_time = datetime.datetime(now.year, now.month, now.day, 10, 30)

print(f"目標: {target_time}")

if target_time > now:
    print("まだ間に合います！")
else:
    print("もう過ぎてしまいました…")