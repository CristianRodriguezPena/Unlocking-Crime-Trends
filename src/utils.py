from datetime import timedelta
import pandas as pd
import matplotlib.pyplot as plt


def mil_time_to_timedelta(mil_time: int) -> timedelta:
    if mil_time < 100:
        return timedelta(minutes=mil_time % 100)
    else:    
        return timedelta(hours=mil_time // 100, minutes=mil_time % 100)
    
    
def number_formatter(value, _=None):
    if value >= 10**6:
        return f"{int(value//(10**6))}M"
    elif value >= 10**4:
        return f"{int(value//(10**3))}k"
    elif value >= 1:
        return f"{int(value)}"
    else:
        return f"{round(100*value, 2)}%"
    
    
def shorten_string(string, max_length=20):
    if len(string) > max_length:
        return string[:max_length] + "..."
    else:
        return string
    
def reorder_cols(cols: list, order_mapping: dict):
    new_cols = cols.copy()
    for item in order_mapping.values():
        new_cols.remove(item)
            
    for index in sorted(order_mapping.keys()):
        new_cols.insert(index, order_mapping[index])
        
    return new_cols

def create_freq_barh(val_counts: pd.Series, ax=None, width=0.8, color="teal"):
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(6, 6))
        
    val_counts.plot.barh(ax=ax, width=width, color=color)
    ax.set_title(val_counts.index.name)
    ax.set_xlabel("Frequency")
    ax.set_ylabel("")
    ax.xaxis.set_major_formatter(number_formatter)
    
    
    for i, count in enumerate(val_counts):
        label = f"{number_formatter(count)}"
        text_x = count * 0.99 if count > val_counts.max()*0.18 else count * 1.01
        text_y = i
        ha = 'right' if count > val_counts.max()*0.175 else 'left'
        ax.text(text_x, text_y, label, ha=ha, va='center', fontsize=8)
    
def hour_num_conv(hour_num: int):
    if hour_num == 0:
        return "Midnight"
    elif hour_num == 12:
        return "Noon"
    
    return f"{(hour_num-1)%12 +1} {"AM" if hour_num < 12 else "PM"}"

def day_of_week_conv(day_num: int):
    days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days_of_the_week[day_num-1]
    
def month_conv(month_num: int):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months[month_num-1]