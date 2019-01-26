FROM rocker/rstudio:latest

RUN R -e "options(repos='http://cran.rstudio.com/')"

# Install swirl
RUN R -e "install.packages('swirl', repos = 'http://cran.us.r-project.org')"

# Install ggplot2
RUN R -e "install.packages('ggplot2', repos = 'http://cran.us.r-project.org')"

# Install RColorBrewer for colorful graphs
RUN R -e "install.packages('RColorBrewer', repos = 'http://cran.us.r-project.org')"

# Install gridExtra package
RUN R -e "install.packages('gridExtra', repos = 'http://cran.us.r-project.org')"

# Install dyplr package
RUN R -e "install.packages('dplyr', repos = 'http://cran.us.r-project.org')"
