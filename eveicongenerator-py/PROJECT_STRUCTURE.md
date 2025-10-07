# 项目结构说明

## 文件列表

```
eveicongenerator-py/
├── __init__.py              # Python包初始化文件
├── cache.py                 # 游戏资源缓存下载模块
├── sde.py                   # SDE数据获取和解析模块
├── icons.py                 # 图标生成核心逻辑
├── main.py                  # 主程序入口
├── requirements.txt         # Python依赖列表
├── README.md                # 使用说明文档
├── PROJECT_STRUCTURE.md     # 本文件
├── .gitignore              # Git忽略文件配置
├── example_usage.sh        # Linux/Mac使用示例脚本
└── example_usage.bat       # Windows使用示例脚本
```

## 模块说明

### cache.py - 缓存模块
**主要类：**
- `CacheError`: 缓存错误异常类
- `IndexEntry`: 索引条目数据类
- `SharedCache`: 共享缓存抽象基类
- `CacheDownloader`: 缓存下载器实现类

**主要功能：**
- 从EVE Online CDN下载游戏资源
- 维护本地文件缓存
- 解析和管理资源索引
- 提供资源查询和访问接口

**关键方法：**
- `__init__()`: 初始化缓存，获取客户端版本和索引
- `fetch()`: 获取资源内容（字节）
- `path_of()`: 获取资源本地路径
- `hash_of()`: 获取资源哈希值
- `has_resource()`: 检查资源是否存在
- `purge()`: 清理过期缓存文件

### sde.py - SDE数据模块
**主要类：**
- `TypeInfo`: 物品类型信息数据类

**主要功能：**
- 从EVE开发者API获取SDE数据
- 解析JSONL格式的游戏数据
- 提取物品类型、分组、图标等信息

**关键函数：**
- `get_sde_version()`: 获取最新SDE版本号
- `download_sde()`: 下载SDE数据包
- `update_sde()`: 更新SDE数据（带版本检查）
- `read_types()`: 读取物品类型信息
- `read_group_categories()`: 读取分组分类映射
- `read_icons()`: 读取图标文件映射
- `read_graphics()`: 读取图形文件夹映射
- `read_skin_materials()`: 读取皮肤材质映射

### icons.py - 图标生成模块
**主要类：**
- `IconKind`: 图标类型枚举
- `IconError`: 图标处理错误异常
- `IconBuildData`: 图标构建数据容器

**主要功能：**
- 图标图像合成和处理
- 多种输出格式生成
- 技术等级覆盖层处理
- 蓝图背景合成

**关键函数：**
- `techicon_resource_for_metagroup()`: 获取技术等级覆盖层资源
- `composite_tech()`: 合成技术等级覆盖层
- `composite_blueprint()`: 合成蓝图图标
- `image_add()`: 图像加法混合
- `build_icon_export()`: 主构建函数
- `_process_blueprint()`: 处理蓝图类型
- `_process_regular_item()`: 处理普通物品
- `_generate_output()`: 生成各种格式输出

**图标类型：**
- ICON: 普通物品图标
- BLUEPRINT: 蓝图图标
- BLUEPRINT_COPY: 蓝图副本图标
- REACTION: 反应蓝图图标
- RELIC: 遗迹图标
- RENDER: 高分辨率渲染图

**输出模式：**
- service_bundle: 服务包（ZIP + 元数据JSON）
- iec: 图像导出集合（标准化命名）
- web_dir: Web托管目录（带索引）
- checksum: MD5校验和
- aux_icons: 辅助图标转储
- aux_all: 所有图像转储

### main.py - 主程序
**主要功能：**
- 命令行参数解析
- 流程控制和协调
- 日志记录
- 错误处理
- 性能统计

**执行流程：**
1. 解析命令行参数
2. 初始化缓存系统
3. 加载SDE数据
4. 构建图标
5. 生成输出
6. 清理临时文件
7. 输出统计信息

## 数据流

```
1. 用户执行命令
   ↓
2. main.py 解析参数
   ↓
3. cache.py 初始化缓存
   ├─ 获取客户端版本
   ├─ 下载索引文件
   └─ 准备资源访问
   ↓
4. sde.py 加载游戏数据
   ├─ 检查SDE版本
   ├─ 下载/更新SDE
   ├─ 解析物品类型
   ├─ 解析分组信息
   ├─ 解析图标映射
   └─ 解析图形资源
   ↓
5. icons.py 构建图标
   ├─ 遍历所有物品类型
   ├─ 确定图标资源
   ├─ 下载资源文件
   ├─ 合成图像
   └─ 生成缓存索引
   ↓
6. icons.py 生成输出
   ├─ service_bundle: ZIP + 元数据
   ├─ iec: 标准化ZIP
   ├─ web_dir: 目录 + 链接
   ├─ checksum: MD5值
   └─ aux_*: 辅助转储
   ↓
7. 输出统计和清理
```

## 与Rust版本的对应关系

| Rust文件 | Python文件 | 说明 |
|---------|-----------|------|
| evesharedcache/src/cache.rs | cache.py | 缓存系统 |
| eveicongenerator/src/sde.rs | sde.py | SDE数据处理 |
| eveicongenerator/src/icons.rs | icons.py | 图标生成 |
| eveicongenerator/src/main.rs | main.py | 主程序 |

## 依赖关系

```
main.py
├── cache.py
│   └── requests
├── sde.py
│   └── requests
└── icons.py
    ├── cache.py
    ├── sde.py
    ├── Pillow (PIL)
    └── numpy
```

## 配置和缓存

**默认目录：**
- 缓存目录: `./cache/`
- 图标目录: `./icons/`

**缓存文件：**
- `cache/sde.zip`: SDE数据包
- `cache/eveonline_*.txt`: 客户端索引
- `cache/...`: 游戏资源文件
- `icons/cache.csv`: 图标索引
- `icons/*.png`: 生成的图标文件

## 性能考虑

**优化点：**
- 增量构建：只处理变更的图标
- 本地缓存：避免重复下载
- 索引机制：快速查找资源
- 批量处理：减少I/O操作

**性能对比：**
- Python版本比Rust版本慢约2-3倍
- 首次运行需要下载大量数据
- 后续运行利用缓存会快很多

## 扩展建议

如需扩展功能，可以：
1. 在`icons.py`中添加新的输出模式
2. 在`sde.py`中添加更多SDE数据解析
3. 在`cache.py`中添加缓存策略
4. 在`main.py`中添加新的命令行选项
