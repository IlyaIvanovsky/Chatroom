name: 漏洞报告
labels:
  - bug
assignees:
  - IlyaIvanovsky
description: 报告漏洞
body:
  - type: input
    id: mversion
    attributes:
      label: 程序版本
      placeholder: 比如 1.2
    validations:
      required: true
  - type: dropdown
    id: type
    attributes:
      label: 你使用的程序类型
      options: 
        - BCM 文件
        - EXE 文件
        - 浏览器运行
    validations:
      required: true
  - type: textarea
    attributes:
      label: Bug 描述
      placeholder: 描述一下你遇到的问题.
    validations:
      required: true
  - type: textarea
    attributes:
      label: 重现步骤
      description: |
        描述怎样做会遇到这个 Bug.
      placeholder: |
        1. 第一步
        2. 第二步
        3. 第三步
  - type: textarea
    attributes:
      label: 其他信息
      description: |
        这个 Bug 的其他信息.
