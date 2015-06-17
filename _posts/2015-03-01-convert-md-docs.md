---
layout: post
title: Convert Markdown Document with Pandoc
tags: python
summary: I find Markdown, a text-to-HTML conversion editor very handy to use. The use of key shortcuts are very intuitive
---

I find Markdown, a text-to-HTML conversion editor very handy to use. The use of key shortcuts are very intuitive and the document renders really well in HTML. I use Markdown to take notes, particularly when I need to copy-paste code. Markdown uses pygments which syntax-highlights the code. Pygments supports over 100 languages.

However, there are few things I do not quite like about markdown. Markdown does not support paragraph justification and conversion to PDF.  Duh! of course, you can't convert to PDF because Markdown is a "text-to-HTML" editor. That is true, but nonetheless, I wanted some program to convert my notes to PDF.

I found Pandoc. Pandoc, written by John MacFarlane, is a "swiss-army knife" to literally convert document from one format to another. What more, I found that when it converts a markdown document to PDF, it justifies the paragraphs automatically and captions each figure with figure numbers. Moreover, Pandoc is free to use. This was a sweet unexpected deal. Here's how one would convert a markdown document to a PDF:

{% highlight python %}
pandoc -V geometry:margin=1in Chapter7_summary.md -o Chapter7.pdf

{% endhighlight python %}

The geometry command sets 1 inch margin on either side. Pandoc is super customizable so you can play with it. 