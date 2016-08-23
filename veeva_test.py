# -*- coding: utf-8 -*-

def is_leap_year(year):
	# 闰年能被4整除,不能被100整除,但可以被400整除
	return (year%4==0) and (year%100!=0) or year%400==0

def year_validation(year):
	# 年须大于等于0
	if year >= 0:
		return True
	return False

def month_validation(month):
	# 月份须在 1 至 12 之间
	if month in xrange(1,13):
		return True 
	return False

def day_validation(month,day,mdays):
	# 日期须小于当月天数并大于0
	if 0 < day <= mdays[month]:
		return True
	return False

def sum_of_days(mdays,month,day):
	mdays = mdays[:month]
	return sum(mdays) + day

def day_of_year(year,month,day):
	"""
    :param year: int
    :param month: int
    :param day: int
    """
	# 每月天数,非闰年
	mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	# 验证输入日期
	if year_validation(year):
		if is_leap_year(year):
			mdays[2] = 29
		if month_validation(month):
			if day_validation(month,day,mdays):
				res = sum_of_days(mdays,month,day)
				return res
			else :
				return ('%s-%s-%s is not a validate date, the given day [%s] is not in the given month [%s-%s].' 
						% (year,month,day,day,year,month))
		else:
			return  ('%s-%s-%s is not a validate date, the given month [%s] should between 1 ~ 12.' 
					% (year,month,day,month))

	return '%s-%s-%s is not a validate date, the given year must greater than 0.' % (year,month,day)


if __name__ == '__main__':
	print day_of_year(2016,12,31)
	print day_of_year(1900,12,31)
	print day_of_year(2016,2,1)
	print day_of_year(2016,2,30)

	