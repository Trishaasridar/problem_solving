monthly_mb = int(input()) # get per month mb
n = int(input()) # get how many months
total_mb = monthly_mb * (n + 1) # cal total
for i in range(n):
    used = int(input()) # per monnth usage of data
    total_mb = total_mb- used
print(total_mb) # print total data available