if (!require("tidyverse")) install.packages("tidyverse")

library(readr)
library(dplyr)
library(ggplot2)

input_folder <- Sys.getenv('CA_INPUT_FOLDER')
print(paste('Input folder:', input_folder))
if (!dir.exists(input_folder)) {
    stop("Invalid input folder")
}

output_folder <- Sys.getenv('CA_OUTPUT_FOLDER')
print(paste('Output folder:', output_folder))
if (!dir.exists(output_folder)) {
    stop("Invalid output folder")
}

# Find and loop through all the CSV files in the input folder
csv_files <- Sys.glob(file.path(input_folder, "*.csv"))
print(paste('Found', length(csv_files), 'CSV files'))

for (i in 1:length(csv_files)) {
    file <- csv_files[i]
    print(paste('Processing:', file))
    
    # Read CSV into a data frame. 
    # Note: We don't do any error checking here.
    df <- read_csv(file)
    # Identify the numeric columns
    df <- select_if(df, is.numeric)

    field_names <- names(df)
    for (j in 1:length(df)) {
        f <- field_names[j]
        print(f)

        plot <-ggplot(df, aes_string(x=paste0('`',f,'`'))) + geom_histogram(alpha = .5,fill = "dodgerblue")
    
        # save to file
        output_path = file.path(output_folder, paste0(tools::file_path_sans_ext(basename(file)), '-', f, '.png'))
        print(paste('Writing plot to:', output_path))
        ggsave(plot, filename=output_path)
    }
}



