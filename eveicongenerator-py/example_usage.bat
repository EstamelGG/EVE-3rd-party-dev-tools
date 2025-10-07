@echo off
REM EVE Icon Generator Python版本使用示例 (Windows)

REM 设置用户代理
set USER_AGENT=MyEVEApp/1.0 (contact@example.com)

REM 示例1: 生成服务包
echo [+] 示例1: 生成服务包
python main.py -u "%USER_AGENT%" service_bundle -o icons_bundle.zip

REM 示例2: 生成IEC格式
echo [+] 示例2: 生成IEC格式
python main.py -u "%USER_AGENT%" iec -o icons_iec.zip

REM 示例3: 生成Web目录（复制文件）
echo [+] 示例3: 生成Web目录
python main.py -u "%USER_AGENT%" web_dir -o ./web_icons --copy_files

REM 示例4: 计算校验和
echo [+] 示例4: 计算校验和
python main.py -u "%USER_AGENT%" checksum -o checksum.txt

REM 示例5: 使用日志文件
echo [+] 示例5: 使用日志文件
python main.py -u "%USER_AGENT%" -l build.log service_bundle -o icons_with_log.zip

REM 示例6: 强制重建
echo [+] 示例6: 强制重建所有图标
python main.py -u "%USER_AGENT%" -f service_bundle -o icons_rebuild.zip

echo [+] 所有示例完成！
pause
