# tget

fofa zoomeye shodan censys 目标采集器

# how to use
1. 写`config/__init__.py`配置文件

2. search语句
```bash
# fofa 搜索
python tget.py fofa -d '"DB_PASSWORD" && title="phpinfo()"' -v --limit 150 -o result.txt

# zoomeye
python tget.py zoomeye -d "thinkphp" -v --limit 10 --type host -o result.txt

# shodan
python tget.py shodan -d "thinkphp" -v --limit 10 -o result.txt

# censys
python tget.py censys -d "thinkphp" -v --limit 120 -o result.txt
```
