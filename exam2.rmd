url=
  "https://fivethirtyeight.com/features/the-polls-werent-great-but-thats-pretty-normal/"
url2 <- read_html(url)

tables <- html_nodes(url2, css = "table")
all.tables=html_table(tables, header = TRUE, fill = TRUE)

seventytwo <- html_table(tables, header = FALSE, fill = TRUE)[[2]]
thirtysix <- html_table(tables, header = FALSE, fill = TRUE)[[3]]

tibbles72 <- 
  as_tibble(seventytwo) %>%
    filter(row_number() != 1) %>%
    rename(Year = X1, FinalAverage = X2, Result = X3, Error = X4) %>%
   mutate(ElectionYear = parse_number(Year),
           FinalAverage = parse_number(FinalAverage),
           Result = parse_number(Result),
           Error = parse_number(Error)
           ) %>%
    select(ElectionYear, FinalAverage, Result, Error)