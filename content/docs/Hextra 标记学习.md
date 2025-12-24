---
title: Hextra 标记学习
type: docs
params:
  math: true
---

- [隐藏页面](#隐藏页面)
- [1. Banner](#1-banner)
- [2. Math](#2-math)
- [3. Hextra Marks](#3-hextra-marks)
  - [3.1. Callout](#31-callout)
  - [3.2. Cards](#32-cards)
  - [3.3. Details](#33-details)
  - [3.4. FileTree](#34-filetree)
  - [3.5. Icon](#35-icon)
  - [3.6. Badge](#36-badge)
  - [3.7. YouTube](#37-youtube)
  - [3.8. PDF](#38-pdf)
  - [3.9. Steps](#39-steps)
    - [3.9.1. Step 1](#391-step-1)
    - [3.9.2. Step 2](#392-step-2)
  - [3.10. Tabs](#310-tabs)
    - [3.10.1. default](#3101-default)
    - [3.10.2. markdown code block](#3102-markdown-code-block)
- [4. Customize shortcodes](#4-customize-shortcodes)


## 隐藏页面
hidden: true 

```
  ---
  title: "不显示在列表"
  date: 2025-12-22
  hidden: true # 仅在主题支持时有效
  ---
```

##  1. <a name='Banner'></a>Banner
hugo.yaml:
```
params:
  banner:
    key: 'announcement-xxx'
    message: |
      🎉 Welcome! [Hextra](https://github.com/hextra/hextra) is a static site generator that helps you build modern websites.
```

The banner will be displayed on all pages.

The field message supports Markdown syntax.

If you want to use template syntax, you can define the partial in layouts/_partials/custom/banner.html. In this case, the field message will be ignored.

##  2. <a name='Math'></a>Math

$1234$

##  3. <a name='HextraMarks'></a>Hextra Marks

###  3.1. <a name='Callout'></a>Callout

{{< callout type="info" >}}
  A **callout** is a short piece of text intended to attract attention.
{{< /callout >}}
{{< callout type="info" >}}
  A **callout** is a short piece of text intended to attract attention.
{{< /callout >}}
{{< callout type="warning" >}}
  A **callout** is a short piece of text intended to attract attention.
{{< /callout >}}
{{< callout type="error" >}}
  A **callout** is a short piece of text intended to attract attention.
{{< /callout >}}
{{< callout type="important" >}} 
  A **callout** is a short piece of text intended to attract attention.
{{< /callout >}}
{{< callout icon="sparkles" >}}
  A **callout** is a short piece of text intended to attract attention.
{{< /callout >}}
{{< callout type="important" icon="sparkles" >}}
  A **callout** is a short piece of text intended to attract attention.
{{< /callout >}}
{{< callout emoji="🌐" >}}
  A **callout** is a short piece of text intended to attract attention.
{{< /callout >}}
{{< callout type="info" emoji="ℹ️" >}}
  A **callout** is a short piece of text intended to attract attention.
{{< /callout >}}




###  3.2. <a name='Cards'></a>Cards 
{{< cards cols="1" >}}
  {{< card link="/" title="Top Card" >}}
  {{< card link="/" title="Bottom Card" >}}
{{< /cards >}}

{{< cards cols="2" >}}
  {{< card link="/" title="Left Card" >}}
  {{< card link="/" title="Right Card" >}}
{{< /cards >}}

{{< cards >}}
  {{< card link="../callout" title="Card with default tag color" tag="tag text" >}}
  {{< card link="../callout" title="Card with red tag" tag="tag text" tagColor="red" >}}
{{< /cards >}}

###  3.3. <a name='Details'></a>Details
{{% details title="Details" %}}

This is the content of the details.

Markdown is **supported**.

{{% /details %}}


{{% details title="Click me to reveal" closed="true" %}}

This will be hidden by default.

{{% /details %}}


###  3.4. <a name='FileTree'></a>FileTree
{{< filetree/container >}}
  {{< filetree/folder name="content" >}}
    {{< filetree/file name="_index.md" >}}
    {{< filetree/folder name="docs" state="closed" >}}
      {{< filetree/file name="_index.md" >}}
      {{< filetree/file name="introduction.md" >}}
      {{< filetree/file name="introduction.fr.md" >}}
    {{< /filetree/folder >}}
  {{< /filetree/folder >}}
  {{< filetree/file name="hugo.toml" >}}
{{< /filetree/container >}}


###  3.5. <a name='Icon'></a>Icon

[List of available icons ](https://github.com/imfing/hextra/blob/main/data/icons.yaml)

{{< icon "github" >}}
{{< icon "warning" >}}
{{< icon "markdown" >}} 

Heroicons v1 outline icons are available out of the box.
[Heroicons](https://v1.heroicons.com/)
[Heroicons v1](https://heroicons.com/solid)

###  3.6. <a name='Badge'></a>Badge
{{< badge "Badge" >}}

{{< badge content="Badge" >}}
{{< badge content="Badge" color="purple" >}}
{{< badge content="Badge" color="indigo" >}}
{{< badge content="Badge" color="blue" >}}
{{< badge content="Badge" color="green" >}}
{{< badge content="Badge" color="yellow" >}}
{{< badge content="Badge" color="amber" >}}
{{< badge content="Badge" color="orange" >}}
{{< badge content="Badge" color="red" >}}

{{< badge content="Badge" icon="sparkles" >}}
{{< badge content="Releases" link="https://github.com/imfing/hextra/releases" icon="github" >}}



###  3.7. <a name='YouTube'></a>YouTube
{{< youtube bUZK9dasP8s >}}

###  3.8. <a name='PDF'></a>PDF 
- PDF test:
- {{< pdf "/PDF/坐标转换.pdf" >}}
- {{< pdf "https://example.com/sample.pdf" >}}

###  3.9. <a name='Steps'></a>Steps

{{< callout type="warning" >}}
 Please note that this shortcode is intended only for Markdown content. If you put HTML content or other shortcodes as step content, it may not render as expected.
{{< /callout >}}

{{% steps %}}

####  3.9.1. <a name='Step1'></a>Step 1

This is the first step.

####  3.9.2. <a name='Step2'></a>Step 2

This is the second step.

{{% /steps %}}


###  3.10. <a name='Tabs'></a>Tabs
####  3.10.1. <a name='default'></a>default
{{< tabs items="JSON,YAML,TOML" >}}

  {{< tab >}}**JSON**: JavaScript Object Notation (JSON) is a standard text-based format for representing structured data based on JavaScript object syntax.{{< /tab >}}
  {{< tab >}}**YAML**: YAML is a human-readable data serialization language.{{< /tab >}}
  {{< tab >}}**TOML**: TOML aims to be a minimal configuration file format that's easy to read due to obvious semantics.{{< /tab >}}

{{< /tabs >}}


####  3.10.2. <a name='markdowncodeblock'></a>markdown code block

{{< tabs items="JSON,YAML,TOML" >}}

  {{< tab >}}
  ```json
  { "hello": "world" }
  ```
  {{< /tab >}}

  ... add other tabs similarly

{{< /tabs >}}



{{< tabs items="A,B" >}}

  {{< tab >}}A content{{< /tab >}}
  {{< tab >}}B content{{< /tab >}}

{{< /tabs >}}

{{< tabs items="A,B" >}}

  {{< tab >}}Second A content{{< /tab >}}
  {{< tab >}}Second B content{{< /tab >}}

{{< /tabs >}}

##  4. <a name='Customizeshortcodes'></a>Customize shortcodes

https://imfing.github.io/hextra/docs/advanced/customization/#component-layout-variables