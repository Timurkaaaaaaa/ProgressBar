<section class="welcome">
  <div class="about" align="center">
      <h1 id="project-name">ProgressBar</h1>
      <h6>Small module for Python</h6>
      a simple tool for displaying task progress in Python console applications. It allows users to see how far the process has progressed, making your code more interactive and usable.
  </div>
  <hr>
  <div class="download">
    <h2>Download:</h2>
    You can install the package using pip. First make sure you have Python and pip installed. Then run the following command:
    <br>
    <pre><code class="bash">pip install TimurkaaaProgressBar</code></pre>
    or download the project source code
  </div>
</section>
<hr>
<section class="examples">
  <h2>Usage:</h2>
  This code shows a small example of use
  <pre><code class="python">import ProgressBar

full = input("Enter the amount of data to download: ")
value = input("Enter the downloaded data: ")
full = int(full)
value = int(value)

ProgressBar.PercentProgressBar(value, full, True)</code></pre>
</section>
<hr>
<section class="end">
  <div>
    <h2>Contribution:</h2>
    If you would like to contribute to the project, please fork the repository, make changes, and create a pull request. We welcome any suggestions and improvements!
  </div>
</section>
