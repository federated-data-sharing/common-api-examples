library(readr)
library(dplyr)
library(ggplot2)

library(rmarkdown)

output_folder <- Sys.getenv('CA_OUTPUT_FOLDER')
print(paste('Output folder:', output_folder))
if (!dir.exists(output_folder)) {
    stop("Invalid output folder")
}

rmarkdown::render('report.Rmd', output_format=html_document(), output_dir=output_folder)

