<h1>This is Lavangam</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/RCReddyN/lavangam/blob/master/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>
<div align="center">
<img src="./img/running.gif">
</div>
<ul>
<li> Lavangam is a command-line spell checker written in Python.
<li> Lavangam, internally, uses a Trie internally to store/search for words.
<li> Thanks to @matthewreagan, whose <a href=https://github.com/matthewreagan/WebstersEnglishDictionary/blob/master/dictionary_alpha_arrays.json>dictionary_alpha_arrays.json</a> I reformated as individual key-value pairs.
<li> Stored words, and their meanings as mongoDB documents. 
<li> Levenshtein's algorithm for minimum distance is used to suggest words.
</ul>

## Usage

```sh
./lavangam
```

## Things you might want to know
<ul>
<li>A <b>Trie</b>, pronounced as "try", is a n-ary tree used to store and search for strings efficiently. Read more about tries <a href= "https://en.wikipedia.org/wiki/Trie#Algorithms">here</a>.
<li><b>Levenshtein's distance</b>, simply refered to as edit-distance, is a metric used to measure difference between two strings. It assumes that the minimum distance is the number of single character edits (insertion, deletion and replacement) required to make two strings equal.
</ul>

## Working
<ul>
<li> In case of correct spelling, the application fetches the meaning from the database.
<li> For an incorrectly spelled word, the application fetches the words closer to it.
</ul>

## Author

👤 **Ravi Chandra N Reddy**
* Website: rcreddyn.github.io
* LinkedIn: [@rcreddyn](https://linkedin.com/in/rcreddyn)
