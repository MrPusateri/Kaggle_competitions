import matplotlib.pyplot as plt

def ut_standard_col_name(input_df):
    '''
    Function to standadize column names of a
    pandas DataFrame.

    Arguments:
    ---
    * input_df (pandas.DataFrame), DataFrame to
        standardise column names.
    '''
    column_names = {i: "_".join(i.split(" ")).lower() for i in input_df.columns}
    return input_df.rename(columns=column_names)

def ut_distinct_elements(input_df):
    '''
    Function that print the number of distinct elements
    for each column in the input DataFrame.

    Arguments:
    ---
    * input_df (pandas.DataFrame), input DataFrame to
        analyse.
    '''
    
    # find maximum length string
    max_len_str = max(input_df.columns, key=len)

    # define header
    header_col_name = "Column Name"
    header_spaces_col_name = " "*(len(max_len_str)-len(header_col_name)+2)
    header_n_distin = "Distinct value count"
    separation_symbols = "-"*len(header_col_name)+header_spaces_col_name+"-"*len(header_n_distin)
    header_str = f"{header_col_name+header_spaces_col_name+header_n_distin}\n{separation_symbols}"
    
    # define body
    output_str = ""
    for i, col_name in enumerate(input_df.columns):
        if col_name==max_len_str:
            col_str = f"{col_name}  {len(input_df.loc[:, col_name].unique())}\n"
        else:
            spaces_to_add = " "*(len(max_len_str)-len(col_name)+2)
            col_str = f"{col_name+spaces_to_add}{len(input_df.loc[:, col_name].unique())}\n"

        if i==len(input_df.columns):
            col_str.replace("\n", "")

        output_str = output_str+col_str
    
    print(header_str)
    print(output_str)


def ut_boxplot_col(input_df, col_to_plot, by=None):
    '''
    Function that creates an image with a boxplot for a
    specific column. We can also specify a specic column
    to group the data.

    Arguments:
    ---
    * input_df (pandas.DataFrame), input DataFrame to
        analyse.
    * col_to_plot (str), column name to plot.
    * by (str), column name to group the data. Default
        is None.
    '''
    fig, ax = plt.subplots(figsize=(5,5), tight_layout=True)
    if by is None:
        input_df.boxplot(column=col_to_plot, ax=ax)
        ax.set(title=f"Box plot of variable: {col_to_plot}")
    else:
        input_df.boxplot(column=col_to_plot, by=by, ax=ax)
    return fig