<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a name="readme-top"></a>

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Author](https://img.shields.io/badge/author-@AymaneElmahi-blue)](https://github.com/AymaneElmahi)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Project Subject](https://img.shields.io/badge/subject-here-svg)](<https://github.com/AymaneElmahi/whats-the-genre/blob/main/Projet-TAL-RI-2023.pdf>)


<!-- PROJECT LOGO -->
<!-- <br />
<div align="center">
  <a href="https://github.com/AymaneElmahi/whats-the-genre">
    <img src="images/logo_written.png" alt="Logo" width="80" height="80">
  </a> -->

<h3 align="center">What's The Genre  </h3>

  <p align="center">
    The aim of this project is to develop a system for retrieving information
    from a collection of film descriptions published on Allociné. The main challenge
    is to automate the classification of films by genre, based on the text of their synopsis
    synopsis and title. This can be a particularly complex task, as film
    film genres can be subtle, and their classification can vary according to
    criteria and contexts.
    To achieve our goal, we will explore several approaches to automatic
    classification approaches and evaluate their suitability using standard
    performance measures. We will also study the text analysis techniques
    best suited to the nature of the data and the needs of the project.
    <br />
    <a href="https://github.com/AymaneElmahi/whats-the-genre"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- <a href="https://github.com/AymaneElmahi/whats-the-genre">View Demo</a> -->
    <a href="https://github.com/AymaneElmahi/whats-the-genre/issues">Report Bug</a>
    <!-- ·
    <a href="https://github.com/AymaneElmahi/whats-the-genre/issues">Request Feature</a> -->
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <!-- <li><a href="#roadmap">Roadmap</a></li> -->
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

The project involves developing a system for retrieving information from a collection
collection of film descriptions from Allociné. It will be divided into two distinct
stages. The first stage will involve the creation of a tool for the automatic classification
based on the text of synopses and titles. To do this, we'll
two CSV files containing descriptions of French-language films provided on Moodle.
provided on Moodle. Different classification algorithms and text
text features will be compared and evaluated according to best practices
such as cross-validation.
The second step will be to apply the selected model to a new dataset
and produce data labeled with the predicted genres. We will
analyze the model's performance in terms of precision, recall and
F1-score. We will also evaluate the model's ability to generalize to new
new datasets, and we'll suggest ways of improving the model's
optimal performance.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

<!-- python, jupyter, tensorflow, pandas -->

[![Python](https://img.shields.io/badge/python-3.9.0-blue)](https://www.python.org/downloads/release/python-390/)  
[![Jupyter](https://img.shields.io/badge/jupyter-6.1.4-orange)](https://jupyter.org/)  
[![Tensorflow](https://img.shields.io/badge/tensorflow-2.4.0-red)](https://www.tensorflow.org/)  
[![Pandas](https://img.shields.io/badge/pandas-1.2.0-yellow)](https://pandas.pydata.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

To install all the required libraries for this project, run the following command:

```sh
pip install -r requirements.txt
```

### Installation

```sh
git clone https://github.com/AymaneElmahi/whats-the-genre.git
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

This project may be used as a starting point for other classification projects. I's also a good example of how to use different classification algorithms and how to evaluate their performance using different performance measures.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## The code is divided into 2 main parts:

### 1. Data preprocessing

- **Data cleaning**: removing duplicates, removing rows with missing values
- **Data exploration**: exploring the data to get a better understanding of the data
- **Data visualization**: visualizing the data to get a better understanding of the data
- **Data preprocessing**: removing stopwords, removing punctuation, tokenization, stemming, lemmatization, vectorization

### 2. Classification

- **Classification**: using different classification algorithms to predict the genre of a movie based on its title and synopsis
- **Evaluation**: evaluating the performance of the different classification algorithms using different performance measures

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Aymane EL MAHI : [Message me on LinkedIn](https://www.linkedin.com/in/aymane-elmahi)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

<!-- ## Acknowledgments

- []()
- []()
- []() -->
<!--
<p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/AymaneElmahi/whats-the-genre.svg?style=for-the-badge
[contributors-url]: https://github.com/AymaneElmahi/whats-the-genre/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AymaneElmahi/whats-the-genre.svg?style=for-the-badge
[forks-url]: https://github.com/AymaneElmahi/whats-the-genre/network/members
[stars-shield]: https://img.shields.io/github/stars/AymaneElmahi/whats-the-genre.svg?style=for-the-badge
[stars-url]: https://github.com/AymaneElmahi/whats-the-genre/stargazers
[issues-shield]: https://img.shields.io/github/issues/AymaneElmahi/whats-the-genre.svg?style=for-the-badge
[issues-url]: https://github.com/AymaneElmahi/whats-the-genre/issues
[license-shield]: https://img.shields.io/github/license/AymaneElmahi/whats-the-genre.svg?style=for-the-badge
[license-url]: https://github.com/AymaneElmahi/whats-the-genre/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/aymane-elmahi
[product-screenshot]: images/about_the_project_screenshot.png
[Flowchart]: images/flowchart.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
