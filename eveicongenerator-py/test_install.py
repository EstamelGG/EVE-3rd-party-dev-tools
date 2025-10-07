#!/usr/bin/env python3
"""
安装测试脚本
验证所有依赖是否正确安装
"""

import sys

def test_python_version():
    """测试Python版本"""
    print("[+] 检查Python版本...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 10):
        print(f"    [x] Python版本过低: {version.major}.{version.minor}.{version.micro}")
        print(f"    [!] 需要Python 3.10或更高版本")
        return False
    print(f"    [✓] Python {version.major}.{version.minor}.{version.micro}")
    return True

def test_imports():
    """测试依赖导入"""
    print("\n[+] 检查依赖包...")
    
    deps = {
        'requests': 'HTTP请求库',
        'PIL': 'Pillow图像处理库',
        'numpy': 'NumPy数值计算库'
    }
    
    all_ok = True
    for module, desc in deps.items():
        try:
            if module == 'PIL':
                import PIL
                version = PIL.__version__
            else:
                mod = __import__(module)
                version = getattr(mod, '__version__', '未知')
            print(f"    [✓] {desc} ({module}) - 版本 {version}")
        except ImportError:
            print(f"    [x] {desc} ({module}) - 未安装")
            all_ok = False
    
    return all_ok

def test_modules():
    """测试项目模块"""
    print("\n[+] 检查项目模块...")
    
    modules = ['cache', 'sde', 'icons']
    all_ok = True
    
    for module in modules:
        try:
            __import__(module)
            print(f"    [✓] {module}.py")
        except Exception as e:
            print(f"    [x] {module}.py - 错误: {e}")
            all_ok = False
    
    return all_ok

def test_main():
    """测试主程序"""
    print("\n[+] 检查主程序...")
    try:
        import main
        print("    [✓] main.py")
        return True
    except Exception as e:
        print(f"    [x] main.py - 错误: {e}")
        return False

def main():
    """主函数"""
    print("=" * 60)
    print("EVE Icon Generator - 安装测试")
    print("=" * 60)
    
    results = []
    
    # 测试Python版本
    results.append(("Python版本", test_python_version()))
    
    # 测试依赖
    results.append(("依赖包", test_imports()))
    
    # 测试模块
    results.append(("项目模块", test_modules()))
    
    # 测试主程序
    results.append(("主程序", test_main()))
    
    # 总结
    print("\n" + "=" * 60)
    print("测试总结")
    print("=" * 60)
    
    all_passed = True
    for name, passed in results:
        status = "[✓] 通过" if passed else "[x] 失败"
        print(f"{status} - {name}")
        if not passed:
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("\n[✓] 所有测试通过！可以开始使用了。")
        print("\n下一步:")
        print("  python main.py -u \"YourApp/1.0\" service_bundle -o test.zip")
        return 0
    else:
        print("\n[x] 部分测试失败，请检查上述错误。")
        print("\n修复建议:")
        print("  1. 确保Python版本 >= 3.10")
        print("  2. 安装依赖: pip install -r requirements.txt")
        print("  3. 检查是否在正确的目录中运行")
        return 1

if __name__ == '__main__':
    sys.exit(main())
