---
title: 扒带记录
type: docs
weight: 3
sidebar:
  open: false
---


- [1. songs](#1-songs)
  - [1.1. 流行-曲子 chord progression](#11-流行-曲子-chord-progression)
  - [1.2. 指弹](#12-指弹)
  - [1.3. 电吉他独奏](#13-电吉他独奏)
- [2. licks](#2-licks)
- [3. Chord Progression 表格渲染 方案](#3-chord-progression-表格渲染-方案)
  - [3.1. markdown 纯文本表格](#31-markdown-纯文本表格)
  - [3.2. markdown 代码块](#32-markdown-代码块)
  - [3.3. HTML 代码，调控更细致](#33-html-代码调控更细致)
  - [3.4. **设置Hugo Table Render Hook + 自定义 表格 css**](#34-设置hugo-table-render-hook--自定义-表格-css)



{{< cards >}}
  {{< card link="./2.1.手指独立性-爬格子左手" title="手指独立性-爬格子左手" icon="academic-cap" >}}
{{< /cards >}}


{{< callout type="warning" >}}
  GTP文件，视频，剪辑 放在 Guitar-Learning-Notebook 仓库；不在Hugo博客内显示
{{< /callout >}}


###  1. <a name='songs'></a>songs
####  1.1. <a name='-chordprogression'></a>流行-曲子 chord progression

####  1.2. <a name=''></a>指弹
- 指法安排，和声构建

####  1.3. <a name='-1'></a>电吉他独奏
- 风格技巧

###  2. <a name='licks'></a>licks



###  3. <a name='ChordProgression'></a>Chord Progression 表格渲染 方案


####  3.1. <a name='markdown'></a>markdown 纯文本表格
| 小节 | 1 | ( + ) | 2 | ( + ) | 3 | ( + ) | 4 | ( + ) | 1 | ( + ) | 2 | ( + ) | 3 | ( + ) | 4 | ( + ) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **级数** | $Imaj^{13}$ | | | | | | $\#I^{\circ 7}$ | | $ii^7$ | | | | $V^7$ | | | |
| **和弦** | $Cmaj^{13}$ | | | | | | $C\#^{\circ 7}$ | | $Dm^7$ | | | | $G^7$ | | | |

| 小节 1 | 拍 1 | 拍 2 | 拍 3 | 拍 4 | ( + ) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **级数** | $I$ | | | | $\#I^{\circ 7}$ |
| **和弦** | $C$ | | | | $C\#^{\circ 7}$ |

####  3.2. <a name='markdown-1'></a>markdown 代码块
```
Key: C Major
[级数] | Imaj13  .       .       #I°7    | ii7     .       .       .       |
[和弦] | Cmaj13  .       .       C#°7    | Dm7     .       .       .       |
拍位:    1       2       3       4         1       2       3       4
       (正拍)          (不在正拍)
```


```
| Measure 1 (4/4)             | Measure 2 (4/4)             |
| [Imaj13] - - - [#I°7]       | [ii7] - - - - - - [V7]      |
|  1   +   2   +   3   +   4  |  1   +   2   +   3   +   4  |
|  ^               ^          |  ^               ^          |
```


####  3.3. <a name='HTML'></a>HTML 代码，调控更细致
<table style="width:100%; border-collapse: collapse; border: 2px solid #333; font-family: sans-serif; text-align: center;">
  <tr style="background-color: #f2f2f2; border-bottom: 2px solid #333;">
    <th style="border: 1px solid #ddd; padding: 8px;">小节</th>
    <th colspan="4" style="border: 1px solid #ddd;">Measure 1</th>
    <th colspan="4" style="border: 1px solid #ddd;">Measure 2</th>
  </tr>
  <tr>
    <td style="font-weight: bold; border: 1px solid #ddd; background-color: #f9f9f9;">级数</td>
    <td colspan="3" style="border: 1px solid #ddd; background-color: #e3f2fd;">$Imaj^{13}$</td>
    <td style="border: 1px solid #ddd; background-color: #fff3e0;">$#I^{\circ 7}$</td>
    <td colspan="4" style="border: 1px solid #ddd;">$ii^7$</td>
  </tr>
  <tr style="border-bottom: 2px solid #333;">
    <td style="font-weight: bold; border: 1px solid #ddd; background-color: #f9f9f9;">和弦</td>
    <td colspan="3" style="border: 1px solid #ddd;">$Cmaj^{13}$</td>
    <td style="border: 1px solid #ddd;">$C\#^{\circ 7}$</td>
    <td colspan="4" style="border: 1px solid #ddd;">$Dm^7$</td>
  </tr>
  <tr style="font-size: 0.8em; color: #888;">
    <td style="border: none;">拍位</td>
    <td style="border: none;">1</td><td style="border: none;">2</td><td style="border: none;">3</td><td style="border: none;">4</td>
    <td style="border: none;">1</td><td style="border: none;">2</td><td style="border: none;">3</td><td style="border: none;">4</td>
  </tr>
</table>


####  3.4. <a name='HugoTableRenderHookcss'></a>**设置Hugo Table Render Hook + 自定义 表格 css**
   - 设置ABCD等多个段落，标记为不同颜色
   - 小节内部透明格线；
   - 小姐之间 实线；
   - 细分 节拍位置，
```markdwon
    | | 1 | 2 | 3 | 4 | 1 | 2 | 3 | 4 |
    | :--- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
    | **和弦** | C | | G | | Am | | F | |
    {meter="44-simple" section="A"}

    | | 1 | 2 | 3 | 4 | 5 | 6 | 1 | 2 | 3 | 4 | 5 | 6 |
    | :--- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
    | **和弦** | C | . | . | G | . | . | Am | . | . | F | . | . |
    {meter="68" section="B"}
```
```css
/* 基础：隐藏所有内部格线 */
.chord-table-wrapper td {
    border: 1px solid transparent;
}

/* --- 4/4 拍逻辑 --- */
/* 假设：1个单元格代表半拍（即一个小节有8格），每8格显示一根实线 */
.chord-table-wrapper[data-meter="44"] td:nth-child(8n+1) {
    border-right: 2px solid #333;
}
/* 如果 1个单元格代表1拍（一个小节4格），则用 4n+1 */
.chord-table-wrapper[data-meter="44-simple"] td:nth-child(4n+1) {
    border-right: 2px solid #333;
}

/* --- 6/8 拍逻辑 --- */
/* 6/8 拍通常 6 个八分音符为一小节，每 6 格显示一根实线 */
.chord-table-wrapper[data-meter="68"] td:nth-child(6n+1) {
    border-right: 2px solid #333;
}
/* 进阶：6/8 拍通常分为两个大拍（3+3），可以给中间加一根虚线 */
.chord-table-wrapper[data-meter="68"] td:nth-child(3n+1):not(:nth-child(6n+1)) {
    border-right: 1px dashed #ccc; 
}

/* 6/8 拍的第1拍和第4拍（大拍）加个淡淡的底色 */
.chord-table-wrapper[data-meter="68"] td:nth-child(6n+2),
.chord-table-wrapper[data-meter="68"] td:nth-child(6n+5) {
    background-color: rgba(0,0,0,0.02);
}

/* 统一：第一列（标题列）永远是实线 */
.chord-table-wrapper td:first-child {
    border-right: 2px solid #333 !important;
}
```
