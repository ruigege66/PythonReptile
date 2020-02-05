from urllib import request

if __name__ == "__main__":
    url = "https://leetcode-cn.com/"
    headers = {
        "cookie":"_ga=GA1.2.606835635.1580743041; gr_user_id=d15dfef5-20a7-44a4-8181-f088825ee052; grwng_uid=1d99b83c-8186-4ffa-905e-c912960d9049; __auc=952db4f31700ba0a3811855dc67; csrftoken=zW1tIWrqqDGQ2gDeEAiRM3Pu41f3qetXjvNP5jxuDpekTTyHj262rmfnO2PtXiCI; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiOTUxOTE1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYXV0aGVudGljYXRpb24uYXV0aF9iYWNrZW5kcy5QaG9uZUF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImQ0ODczNmFiODAwZjk0ZTU3ZjAwMmQ4YjU1YjRmNWZmMDViMDllOTIiLCJpZCI6OTUxOTE1LCJlbWFpbCI6IiIsInVzZXJuYW1lIjoicnVpZ2VnZTY2IiwidXNlcl9zbHVnIjoicnVpZ2VnZTY2IiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUtY24uY29tL2FsaXl1bi1sYy11cGxvYWQvZGVmYXVsdF9hdmF0YXIucG5nIiwicGhvbmVfdmVyaWZpZWQiOnRydWUsInRpbWVzdGFtcCI6IjIwMjAtMDItMDMgMTU6MTg6MDYuNjYwMDkxKzAwOjAwIiwiUkVNT1RFX0FERFIiOiIxNzIuMjEuNS4xOTUiLCJJREVOVElUWSI6IjdiMTc5MTc2MTVmNTU1NDRiNjA1ZjFhNjc0NzdjMmU0IiwiX3Nlc3Npb25fZXhwaXJ5IjoxMzgyNDAwfQ.NmZ7AjH_bglQEjMY9CQSoULGfmbXgmaLzu5TamQ5hVo; a2873925c34ecbd2_gr_last_sent_cs1=ruigege66; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1580743040,1580917807; __asc=f5041e12170160b58f59beeae32; a2873925c34ecbd2_gr_session_id=e9ba4267-3dbc-47c1-aa02-c6e92e8eb4a8; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=e9ba4267-3dbc-47c1-aa02-c6e92e8eb4a8; a2873925c34ecbd2_gr_session_id_e9ba4267-3dbc-47c1-aa02-c6e92e8eb4a8=true; _gid=GA1.2.1242221115.1580917808; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1580917870; a2873925c34ecbd2_gr_cs1=ruigege66; _gat_gtag_UA_131851415_1=1"
    }
    req = request.Request(url,headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    with open("rsp.html","w") as f:
        f.write(html.encode("GBK","ignore").decode("GBK"))
