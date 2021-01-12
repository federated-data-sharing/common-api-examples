# boxplot assuming combined output of data-profiler
library(ggplot2)

post_process = function(df_) {
    g <- ggplot(df_) +
        geom_boxplot(aes(   ymin    = min, 
                            lower   = `25%`, 
                            middle  = `50%`, 
                            upper   = `75%`, 
                            ymax    = max, 
                            x       = field_name), 
                        stat = "identity")
    return(g)
}
