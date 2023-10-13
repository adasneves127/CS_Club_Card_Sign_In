def get_col_widths(results: list) -> list:
    """Get the column widths for the results"""
    widths = []
    for i in range(len(results[0])):
        widths.append(max([len(str(x[i])) for x in results]))
    return widths
