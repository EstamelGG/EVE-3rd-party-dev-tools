# 快速开始指南

## 5分钟上手EVE Icon Generator

### 步骤1: 检查Python版本
```bash
python --version
# 或
python3 --version
```
确保版本 >= 3.10

### 步骤2: 安装依赖
```bash
# Windows
pip install -r requirements.txt

# Linux/Mac
pip3 install -r requirements.txt
```

### 步骤3: 运行第一个命令
```bash
# Windows
python main.py -u "MyApp/1.0" service_bundle -o icons.zip

# Linux/Mac
python3 main.py -u "MyApp/1.0" service_bundle -o icons.zip
```

**注意：** 首次运行会下载约2-3GB的游戏数据，请耐心等待。

### 步骤4: 查看输出
生成的`icons.zip`包含：
- 所有图标PNG文件
- `service_metadata.json`元数据文件

## 常见使用场景

### 场景1: 为Web应用准备图标
```bash
python main.py -u "MyWebApp/1.0" web_dir -o ./public/icons --copy_files
```
生成的目录可直接用于Web服务。

### 场景2: 获取特定物品的图标
1. 先生成IEC格式：
```bash
python main.py -u "MyApp/1.0" iec -o icons.zip
```

2. 解压后查找：
- `34_64.png` - 物品ID 34的图标
- `34_bpc_64.png` - 物品ID 34的蓝图副本图标

### 场景3: 定期更新图标
```bash
# 使用日志记录更新
python main.py -u "MyApp/1.0" -l update.log -s service_bundle -o icons.zip
```
`-s`参数会在图标未变化时跳过输出。

### 场景4: 验证图标完整性
```bash
# 生成校验和
python main.py -u "MyApp/1.0" checksum -o checksum.txt

# 下次运行后对比
python main.py -u "MyApp/1.0" checksum -o checksum_new.txt
diff checksum.txt checksum_new.txt
```

## 常见问题

### Q: 下载速度很慢怎么办？
A: 这是正常的，游戏资源文件很大。建议：
- 使用有线网络
- 在网络空闲时运行
- 首次运行后会缓存，后续会快很多

### Q: 出现"资源未找到"错误？
A: 可能原因：
- 网络连接问题
- CCP服务器维护
- 缓存损坏（删除`./cache`目录重试）

### Q: 内存不足？
A: 尝试：
- 关闭其他程序
- 使用64位Python
- 增加系统虚拟内存

### Q: 如何只生成部分图标？
A: 目前不支持，但可以：
1. 生成完整的IEC格式
2. 从ZIP中提取需要的图标

### Q: 输出文件很大？
A: 是的，完整图标集约500MB-1GB。可以：
- 使用`web_dir`模式生成链接而非复制
- 只保留需要的图标类型
- 压缩输出文件

## 进阶用法

### 使用配置文件
创建`config.sh`（Linux/Mac）：
```bash
#!/bin/bash
export USER_AGENT="MyApp/1.0"
export CACHE_DIR="./my_cache"
export ICON_DIR="./my_icons"

python main.py -u "$USER_AGENT" \
    -c "$CACHE_DIR" \
    -i "$ICON_DIR" \
    "$@"
```

使用：
```bash
chmod +x config.sh
./config.sh service_bundle -o output.zip
```

### 自动化脚本
创建`auto_update.sh`：
```bash
#!/bin/bash
DATE=$(date +%Y%m%d)
python main.py -u "AutoUpdate/1.0" \
    -l "logs/update_$DATE.log" \
    -s \
    service_bundle -o "output/icons_$DATE.zip"
```

### 与其他工具集成
```python
# 在Python脚本中使用
import subprocess
import json

# 生成图标
subprocess.run([
    'python', 'main.py',
    '-u', 'MyScript/1.0',
    'service_bundle',
    '-o', 'icons.zip'
])

# 读取元数据
import zipfile
with zipfile.ZipFile('icons.zip', 'r') as zf:
    metadata = json.loads(zf.read('service_metadata.json'))
    print(f"生成了 {len(metadata)} 个物品的图标")
```

## 下一步

- 阅读完整文档：[README.md](README.md)
- 了解项目结构：[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)
- 查看示例脚本：`example_usage.sh` / `example_usage.bat`

## 获取帮助

```bash
# 查看所有选项
python main.py --help

# 查看特定子命令的帮助
python main.py service_bundle --help
python main.py web_dir --help
```
