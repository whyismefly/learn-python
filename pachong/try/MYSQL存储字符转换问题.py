#!/usr/bin/python3
# encoding:utf-8

string1 ="""存、转运、处置等各环节管理人员职责，确保责任落实到位。相关部门要加大对医疗废物管理的督查力度，督促各项管理制度落实到位，
重点强化医疗废物去向监督，坚决杜绝流出、倒卖或倾倒现象。', '\n\u3000\u3000七、完善医疗废物收集处置保障措施。各医疗废物集中处置单位应
加强物资储备。各市、县要积极协调，保障医疗废物收集、转运、处置过程中所需的各类物资。在疫情结束后，由医疗废物集中处置单位进行成本核算，
经审核后，由市级人民政府给予补贴。', '\n', '\n ', '\n\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000
\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000 关于应对新型冠状病毒肺炎疫情', '\n\u3000\u3000\u3000
\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000 支持中小微企业平稳
健康发展的若干措施', '\n ', '\n一、加大金融支持', '\n\u3000\u30001﹒加大信贷支持力度。制定普惠型小微企业贷款增长目标，实施差异化绩效
考核办法，确保商业银行普惠型小微企业贷款增速不低于各项贷款增速。加强对制造业、小微企业等重点领域信贷支持，加大信用贷款和中长期贷款投放
力度，建立绩效考核与信贷投放挂钩激励机制，推动333"""

string2 ="""存、转运、处置等各环节管理人员职责，确保责任落实到位。相关部门要加大对医疗废物管理的督查力度，督促各项管理制度落实到位，
重点强化医疗废物去向监督，坚决杜绝流出、倒卖或倾倒现象。', '\n\u3000\u3000七、完善医疗废物收集处置保障措施。各医疗废物集中处置单位应
加强物资储备。各市、1111"""


print(string1.replace(u'\u3000', u'') )
string2 = string2 + string1
print(string2)
string3=[]
print(string3[0])
