# tget

fofa zoomeye shodan censys 目标采集器

# how to use

1.download

```bash
git clone https://github.com/saucer-man/tget
cd tget
python3 -m pip install -r requirements.txt --upgrade
```

2.写`config/__init__.py`配置文件

3.search example

```bash
# fofa
python tget.py fofa -d "\"DB_PASSWORD\" && title=\"phpinfo()\"" -v --limit 150 -o result.txt

# zoomeye
python tget.py zoomeye -d "\"DB_PASSWORD\" && title=\"phpinfo()\""  -v --limit 10 --type host -o result.txt

# shodan
python tget.py shodan -d "\"DB_PASSWORD\" && title=\"phpinfo()\""  -v --limit 10 -o result.txt

# censys
python3 tget.py censys -d "service.service_name: HTTP"  -v --limit 10 -o result.txt
```
