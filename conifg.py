# -*- coding: utf-8 -*-
# @Time : 2022-03-08 12:08 
# @Author : YD


from pydantic import BaseModel


class _Setting(BaseModel):
    branch_name = 'branch'
    update_time = '2022-03-08 12:35'


setting = _Setting()

__all__ = ['setting']
