#!/bin/bash

# 1.下载pyenv到你想要安装的目录,我安装到了$HOME/.pyenv
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# 2.定义环境变量PYENV_ROOT，指向pyenv安装目录。
# 并且将$PYENV_ROOT/bin追加到系统环境变量$PATH,用于使用pyenv命令行工具
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile

# 3.将pyenv init添加到shell中以启用shims和自动补全功能
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile

# 4.重启shell,使之前的配置得以生效
exec "$SHELL"
