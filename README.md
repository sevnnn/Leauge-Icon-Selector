# League Icon Selector

Simple League Of Legends application to help you pick your summoner icon

## Requirements

- Python 3.11
- Poetry (use `pip install poetry` if you dont have it installed)

## Installation

1. Clone this repo

```bash
> git clone https://github.com/sevnnn/Leauge-Icon-Selector.git
> cd League-Icon-Selector 
```

2. Install required packages
```bash
> poetry install --without=dev
```
<sup>You can also install it with development packages by removing `--without=dev` if your planning on modifying the code</sup>

3. Make sure that settings in [config.json](./config.json) are valid

## Usage

```bash
> poetry run flask --app league-icon-selector run
```

## Features

<details>

<summary>Example usage</summary>

![example usage](/readme/example.gif)

</details>

<br>

- Shows only icons you own (and [Helmet Bro](https://cdn.communitydragon.org/latest/profile-icon/29))
- Filter icons by name
- Select random icon
- Set your icon right in the browser
