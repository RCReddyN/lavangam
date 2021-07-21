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
<li> An elephantine collection of words from NLTK corpus, is used to contruct the trie, so expect a second delay.
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
<li> Get a demo of how Lavangam works from a <a href = "https://telegram.me/thegrailbot">telegram bot</a> I wrote.
<li> Type in a word you want to check for a potential incorrect spelling.
</ul>
<div align="center">
<img src = "https://github.com/RCReddyN/lavangam/blob/master/img/lavangam.png">
</div>

## The Story
<p>Years ago, I came across a problem on <a href="https://leetcode.com/problems/edit-distance">Leetcode</a>, that I couldn't solve at first. I revisted the problem few days later and I solved it using recursion. I felt so happy, that in excitement, I implemented all the applications. I picked up spellchecker again when I was learning about Tries. When I implemented this as a commandline application, I realized that this recursive implementation is too slow. The very next day, I optimized the algorithm using DP(I very recently learnt that this DP implementation has a name - Wagner Fischer Algorithm). Again, months later, I implemented Damerau-Levenshtein's Distance. Today, it stands tall, but tomorrow I do not know. May be, I will stumble upon more efficient and correct algorithm. Don't forget to revisit in a few days.</p>  

## Author

👤 **Ravi Chandra N Reddy**
* Website: rcreddyn.github.io
* LinkedIn: [@rcreddyn](https://linkedin.com/in/rcreddyn)
