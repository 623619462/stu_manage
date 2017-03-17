# -*- coding: utf-8 -*-
stu_dict={u'姓名':'name',u'曾用名':'usedName',u'班号':'class',u'专业':'major',u'身份证件号':'id',u'性别':'gender',u'出生日期':'birth',u'民族':'nation',u'政治面貌':'polity',u'生源国':'nationality',u'生源省':'province',u'籍贯':'nativePlace',u'考生类别':'stuTypeb',u'考生类型':'stuTypex',u'助学贷款':'loan',u'原户口所在地':'domPlace',u'现户口所在地':'domPlaceNew',u'户口迁移':'domMove',u'何省市报考':'registplace',u'入学前单位':'highSchool',u'邮箱':'email',u'QQ':'qq',u'手机':'phone',u'家庭地址':'address',u'家庭邮编':'postcode',u'家庭电话':'homePhone',u'父亲姓名':'faName',u'父亲工作单位':'faWorkUnit',u'父亲工作职务':'faJob',u'父亲电话':'faPhone',u'母亲姓名':'maName',u'母亲工作单位':'maWorkUnit',u'母亲工作职务':'maJob',u'母亲电话':'maPhone',u'其他家庭成员姓名':'otherMember',u'其他家庭成员与本人关系':'otherRelation',u'其他家庭成员工作单位':'otherWorkUnit',u'其他家庭成员职务':'otherJob',u'其他家庭成员电话':'otherPhone',u'住宿（校区）':'campus',u'住宿（栋）':'building',u'住宿（号）':'room',u'学业成绩':'grade',u'学籍异动':'roll',u'助学金':'stipend',u'奖学金':'scholarship',u'获奖经历':'honour',u'干部经历':'leader',u'出境经历':'abroad',u'学术经历':'academic',u'实习经历':'practice',u'毕业去向':'career',u'谈话记录':'talk',u'备注':'remark',u'特长':'specialty'}
name_dict={'faName': u'\u7236\u4eb2\u59d3\u540d', 'major': u'\u4e13\u4e1a', 'faJob': u'\u7236\u4eb2\u5de5\u4f5c\u804c\u52a1', 'domPlaceNew': u'\u73b0\u6237\u53e3\u6240\u5728\u5730', 'grade': u'\u5b66\u4e1a\u6210\u7ee9', 'loan': u'\u52a9\u5b66\u8d37\u6b3e', 'roll': u'\u5b66\u7c4d\u5f02\u52a8', 'domMove': u'\u6237\u53e3\u8fc1\u79fb', 'postcode': u'\u5bb6\u5ead\u90ae\u7f16', 'otherJob': u'\u5176\u4ed6\u5bb6\u5ead\u6210\u5458\u804c\u52a1', 'campus': u'\u4f4f\u5bbf\uff08\u6821\u533a\uff09', 'leader': u'\u5e72\u90e8\u7ecf\u5386', 'abroad': u'\u51fa\u5883\u7ecf\u5386', 'stuTypeb': u'\u8003\u751f\u7c7b\u522b', 'id': u'\u8eab\u4efd\u8bc1\u4ef6\u53f7', 'maJob': u'\u6bcd\u4eb2\u5de5\u4f5c\u804c\u52a1', 'stuTypex': u'\u8003\u751f\u7c7b\u578b', 'registplace': u'\u4f55\u7701\u5e02\u62a5\u8003', 'otherWorkUnit': u'\u5176\u4ed6\u5bb6\u5ead\u6210\u5458\u5de5\u4f5c\u5355\u4f4d', 'email': u'\u90ae\u7bb1', 'nativePlace': u'\u7c4d\u8d2f', 'province': u'\u751f\u6e90\u7701', 'maPhone': u'\u6bcd\u4eb2\u7535\u8bdd', 'building': u'\u4f4f\u5bbf\uff08\u680b\uff09', 'name': u'\u59d3\u540d', 'honour': u'\u83b7\u5956\u7ecf\u5386', 'practice': u'\u5b9e\u4e60\u7ecf\u5386', 'specialty': u'\u7279\u957f', 'stipend': u'\u52a9\u5b66\u91d1', 'nation': u'\u6c11\u65cf', 'polity': u'\u653f\u6cbb\u9762\u8c8c', 'faWorkUnit': u'\u7236\u4eb2\u5de5\u4f5c\u5355\u4f4d', 'maName': u'\u6bcd\u4eb2\u59d3\u540d', 'birth': u'\u51fa\u751f\u65e5\u671f', 'address': u'\u5bb6\u5ead\u5730\u5740', 'nationality': u'\u751f\u6e90\u56fd', 'usedName': u'\u66fe\u7528\u540d', 'otherPhone': u'\u5176\u4ed6\u5bb6\u5ead\u6210\u5458\u7535\u8bdd', 'class': u'\u73ed\u53f7', 'homePhone': u'\u5bb6\u5ead\u7535\u8bdd', 'domPlace': u'\u539f\u6237\u53e3\u6240\u5728\u5730', 'qq': u'QQ', 'remark': u'\u5907\u6ce8', 'room': u'\u4f4f\u5bbf\uff08\u53f7\uff09', 'faPhone': u'\u7236\u4eb2\u7535\u8bdd', 'phone': u'\u624b\u673a', 'career': u'\u6bd5\u4e1a\u53bb\u5411', 'gender': u'\u6027\u522b', 'otherRelation': u'\u5176\u4ed6\u5bb6\u5ead\u6210\u5458\u4e0e\u672c\u4eba\u5173\u7cfb', 'maWorkUnit': u'\u6bcd\u4eb2\u5de5\u4f5c\u5355\u4f4d', 'otherMember': u'\u5176\u4ed6\u5bb6\u5ead\u6210\u5458\u59d3\u540d', 'academic': u'\u5b66\u672f\u7ecf\u5386', 'highSchool': u'\u5165\u5b66\u524d\u5355\u4f4d', 'talk': u'\u8c08\u8bdd\u8bb0\u5f55', 'scholarship': u'\u5956\u5b66\u91d1','stu_id':u'学号'}

