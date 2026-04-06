# from datetime import datetime, timezone

# utc = datetime.now(timezone.utc)
# local = datetime.now()
# print("Aditya singh")
# print("UTC:", utc)
# print("Local:", local)

from datetime import datetime, timezone
import zoneinfo

utc_time = datetime.now(timezone.utc)

ist = utc_time.astimezone(zoneinfo.ZoneInfo("Asia/Kolkata"))
print(ist) 