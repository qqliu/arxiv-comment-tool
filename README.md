# arxiv-comment-tool

This tool removes comments prepended by "%", \iffalse and other customized \if statements, and custom (todo) commands from LaTeX source files. 

<em>Parameters</em>

1. --filename: list of space-separated filenames of LaTeX files you would like to remove comments...etc.
2. --folder: folder name of the folder you want the sanitized LaTeX files to reside.
3. --encoding: text encoding (default: utf-8)

<em>Disclaimer</em> This tool has not been widely tested for many types files. There may be bugs/unintended deletions depending on the file. The author(s) do not hold responsibility for any unintended results that may occur while using this file. We encourage you to help us improve this tool by submitting pull requests. 
