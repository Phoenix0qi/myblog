---
title: Hextra 标记学习
type: docs
params:
  math: true
---


# Math

$1234$

# Hextra Marks

## Callout

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




## Cards 
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

## Details
{{% details title="Details" %}}

This is the content of the details.

Markdown is **supported**.

{{% /details %}}


{{% details title="Click me to reveal" closed="true" %}}

This will be hidden by default.

{{% /details %}}


## FileTree
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


## Icon

[List of available icons ](https://github.com/imfing/hextra/blob/main/data/icons.yaml)

{{< icon "github" >}}
{{< icon "warning" >}}
{{< icon "markdown" >}} 

Heroicons v1 outline icons are available out of the box.
[Heroicons](https://v1.heroicons.com/)
[Heroicons v1](https://heroicons.com/solid)

## Badge
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



## YouTube
{{< youtube bUZK9dasP8s >}}

## PDF 
- PDF test:
- {{< pdf "/PDF/坐标转换.pdf" >}}
- {{< pdf "https://example.com/sample.pdf" >}}

## Steps

{{< callout type="warning" >}}
 Please note that this shortcode is intended only for Markdown content. If you put HTML content or other shortcodes as step content, it may not render as expected.
{{< /callout >}}

{{% steps %}}

### Step 1

This is the first step.

### Step 2

This is the second step.

{{% /steps %}}


## Tabs
### default
{{< tabs items="JSON,YAML,TOML" >}}

  {{< tab >}}**JSON**: JavaScript Object Notation (JSON) is a standard text-based format for representing structured data based on JavaScript object syntax.{{< /tab >}}
  {{< tab >}}**YAML**: YAML is a human-readable data serialization language.{{< /tab >}}
  {{< tab >}}**TOML**: TOML aims to be a minimal configuration file format that's easy to read due to obvious semantics.{{< /tab >}}

{{< /tabs >}}


### markdown code block

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

# Customize shortcodes

https://imfing.github.io/hextra/docs/advanced/customization/#component-layout-variables