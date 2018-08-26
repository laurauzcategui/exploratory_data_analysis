FROM rocker/rstudio:latest

# Install swirl
RUN R -e "install.packages('swirl', repos = 'http://cran.us.r-project.org')"

# Install ggplot2
RUN R -e "install.packages('ggplot2', repos = 'http://cran.us.r-project.org')"

# Install RColorBrewer for colorful graphs
RUN R -e "install.packages('RColorBrewer', repos = 'http://cran.us.r-project.org')"
