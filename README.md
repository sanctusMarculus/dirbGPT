<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>dirbGPT</h1>

<p>
    <strong>dirbGPT</strong> is a tool that scans a website for hidden directories using Selenium and OpenAI's GPT-3.5-turbo. It generates a wordlist based on the paths found on the website and then uses this wordlist to find hidden directories.
</p>

<h2>Requirements</h2>
<ul>
    <li>Python 3.7+</li>
    <li>OpenAI Python library</li>
    <li>Selenium</li>
    <li>Webdriver Manager</li>
    <li>Requests</li>
</ul>

<h2>Installation</h2>
<p>To install the required libraries, run:</p>
<pre><code>pip install openai selenium webdriver-manager requests</code></pre>

<h2>Usage</h2>
<ol>
    <li>Set your OpenAI API key as an environment variable:</li>
</ol>
<pre><code>export OPENAI_API_KEY="your-api-key"</code></pre>
<ol start="2">
    <li>Run the script:</li>
</ol>
<pre><code>python script_name.py https://example.com</code></pre>

<h2>Output</h2>
<ul>
    <li><code>extended_wordlist.txt</code>: The generated wordlist based on the website paths.</li>
    <li><code>found_dirs.txt</code>: The hidden directories found on the website.</li>
</ul>

<h2>Script Explanation</h2>
<p>The <code>dirbGPT</code> script performs the following steps:</p>
<ol>
    <li>Scans the provided website URL using Selenium to extract all paths.</li>
    <li>Generates a wordlist based on the scanned paths using OpenAI's GPT-3.5-turbo.</li>
    <li>Saves the generated wordlist to <code>extended_wordlist.txt</code>.</li>
    <li>Uses the generated wordlist to scan for hidden directories on the website.</li>
    <li>Saves the found directories to <code>found_dirs.txt</code>.</li>
</ol>


</body>
</html>
