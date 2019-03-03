# word_score_calculator
Knowledge, Hard Work, Money...whatever. They say only Attitude is 100%

# remark-usage

[![Build][build-badge]][build]
[![Coverage][coverage-badge]][coverage]
[![Downloads][downloads-badge]][downloads]
[![Chat][chat-badge]][chat]
[![Sponsors][sponsors-badge]][collective]
[![Backers][backers-badge]][collective]

Add a [usage][] example to a README with [**remark**][remark].

## Installation

[npm][]:

```bash
npm install remark-usage
```

## Usage

This section is rendered by this module from [example.js][example-js].

Dependencies:

```javascript
var fs = require('fs')
var remark = require('remark')
var usage = require('remark-usage') // This is changed from `./index.js` to `remark-usage`
```

Read and parse `readme.md`:

```javascript
var readme = fs.readFileSync('readme.md', 'utf-8')
var ast = remark()
  .use(usage)
  .parse(readme)
```

