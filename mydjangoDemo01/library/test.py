# python mydjangoDemo01/manage.py  test mydjangoDemo01 library

from django.test import TestCase

class Demo(TestCase):
    def setUp(self):
        #print('setUp')
        pass

    # Create your tests here.
    def test_getInformationOption(self):
        # 检查context可用的键
        from .log2index import getInformationOption
        context=getInformationOption()
        keys=context.keys()
        print("=> login页面获取的信息:",keys)

    def test_startend2mask(self):
        from .adminIndex import startend2mask
        start=9
        end=11
        mask="00000000011100000000000000"
        mask_lab=startend2mask(start,end)
        if mask_lab==mask:
            print("=> startend2mask函数通过测试")
        else:
            print("=> 请重新检查startend2mask函数")
    def test_mask2startend(self):
        from .adminIndex import mask2startend
        start=9
        end=11
        mask="00000000011100000000000000"
        start_lab,end_lab=mask2startend(mask)
        if start_lab==start and end_lab==end:
            print("=> mask2startend函数通过测试")
        else:
            print("=> 请重新检查mask2startend函数")

    def test_human_read_accessable(self):
        from .studentIndex import human_read_accessable
        accessable=['9','10','11','13','14','15','20']
        h_accessable=str([[9,11],[13,15],[20,20]])
        pre_accessable=human_read_accessable(accessable)
        if h_accessable==pre_accessable:
            print("=> test_human_read_accessable函数通过测试")
        else:
            print("=> 请重新检查test_human_read_accessable函数")

    def test_seatAvailable(self):
        from .studentIndex import seatAvailable
        Mask="00000000011100000000000000"
        Used="00000000011100000000000000"
        Start=10
        End=15
        available=False
        pre_available=seatAvailable(Mask,Used,Start,End)
        if pre_available==available:
            print("=> seatAvailable函数通过测试")
        else:
            print("=> 请重新检查seatAvailable函数")

    def test_seat_management(self):
        """测试座位管理相关功能"""
        try:
            from .models import SeatInfo
            # 测试添加座位
            test_seat = SeatInfo.objects.create(
                Campus="测试校区",
                Classroom="A101",
                Index="001001",
                Electricity=True,
                Mask="00000000011100000000000000",
                MaxTime=4
            )
            print("=> 座位添加测试通过")
            
            # 测试座位查询
            seat = SeatInfo.objects.get(Campus="测试校区", Classroom="A101")
            if seat.Index == "001001" and seat.Electricity == True:
                print("=> 座位查询测试通过")
            else:
                print("=> 座位查询测试失败")
                
            # 清理测试数据
            test_seat.delete()
        except Exception as e:
            print(f"=> 座位管理测试失败: {str(e)}")

    def test_reservation_time(self):
        """测试预约时间相关功能"""
        try:
            from .adminIndex import startend2mask
            from .studentIndex import seatAvailable
            
            # 测试不同时间段的座位可用性
            test_cases = [
                {
                    "mask": "00000000011100000000000000",
                    "used": "00000000000000000000000000",
                    "start": 9,
                    "end": 12,
                    "expected": True
                },
                {
                    "mask": "00000000011100000000000000",
                    "used": "00000000011100000000000000",
                    "start": 9,
                    "end": 12,
                    "expected": False
                }
            ]
            
            for case in test_cases:
                result = seatAvailable(case["mask"], case["used"], case["start"], case["end"])
                if result == case["expected"]:
                    print(f"=> 预约时间测试通过: {case}")
                else:
                    print(f"=> 预约时间测试失败: {case}")
        except Exception as e:
            print(f"=> 预约时间测试失败: {str(e)}")

    def test_human_readable_format(self):
        """测试人类可读格式转换功能"""
        try:
            from .studentIndex import human_read_accessable
            
            test_cases = [
                {
                    "input": ['1', '2', '3', '5', '6', '8'],
                    "expected": "[[1, 3], [5, 6], [8, 8]]"
                },
                {
                    "input": ['1', '2', '3', '4', '5'],
                    "expected": "[[1, 5]]"
                }
            ]
            
            for case in test_cases:
                result = human_read_accessable(case["input"])
                if result == case["expected"]:
                    print(f"=> 人类可读格式测试通过: {case}")
                else:
                    print(f"=> 人类可读格式测试失败: {case}")
        except Exception as e:
            print(f"=> 人类可读格式测试失败: {str(e)}")
    def test_sendemail(self):
        from smtplib import SMTPException
        from sendemail import sendemail
        Head = "自习室管理系统自动邮箱 - 测试邮件"
        Context = "这是一封测试邮件，来自你的 Django 项目。"
        ToAddress = "收件人邮箱@example.com"  # 请改为你自己的真实收件邮箱

        try:
            sendemail(Head=Head, Context=Context, ToAddress=ToAddress)
            print("✅ 测试邮件发送成功，请检查邮箱收件箱。")
        except SMTPException as e:
            print(f"❌ 发送失败，SMTP错误：{e}")
        except Exception as e:
            print(f"❌ 发送失败，其他错误：{e}")
    def test_inCampus(self):
        from .studentIndex import inCampus
        result = inCampus(None)
        if result is True:
            print("✅ 校内函数测试通过")
        else:
            print("❌ 校内函数测试未通过")
    def test_reservation_time_validation(self):
        from .studentIndex import is_reservation_time_valid
        print("正在生成随机化预约时间测试样例......")
        test_cases = [
            {"start": 9, "end": 11, "max_time": 4, "available_start": 8, "available_end": 22, "expected": True},
            {"start": 12, "end": 10, "max_time": 4, "available_start": 8, "available_end": 22, "expected": False},
            {"start": 7, "end": 9, "max_time": 4, "available_start": 8, "available_end": 22, "expected": False},
            {"start": 9, "end": 15, "max_time": 4, "available_start": 8, "available_end": 22, "expected": False},
            {"start": 9, "end": 11, "max_time": 4, "available_start": 10, "available_end": 22, "expected": False},
            {"start": 9, "end": 23, "max_time": 4, "available_start": 8, "available_end": 22, "expected": False},
        ]

        for i, case in enumerate(test_cases):
            result, msg = is_reservation_time_valid(
                case["start"], case["end"], case["max_time"], case["available_start"], case["available_end"]
            )
            passed = result == case["expected"]
            print("=" * 50)
            print(f"🧪 测试用例 {i+1}")
            print(f"输入参数:")
            print(f"  ⏰ start = {case['start']}, end = {case['end']}")
            print(f"  ⏳ max_time = {case['max_time']}")
            print(f"  🏫 available_start = {case['available_start']}, available_end = {case['available_end']}")
            print(f"期望结果: {case['expected']}  实际结果: {result}")
            if passed:
                print(f"✅ 测试通过")
            else:
                print(f"❌ 测试失败")
                print(f"📩 错误信息: {msg}")
            print("=" * 50 + "\n")
    def test_get_remind_time():
        from apscheduler import getRemindTime
        remind_time = getRemindTime(15)
        print(f"提醒时间: {remind_time}")  # 观察输出时间是否合逻辑

    def test_get_deadline():
        from apscheduler import getDeadline
        deadline = getDeadline(15)
        print(f"截止时间: {deadline}")  # 观察输出时间是否合逻辑
    def test_occupy_and_release_seat():
        from apscheduler import occupySeat, releaseSeat
        class DummySeat:
            def __init__(self):
                self.Used = "0" * 24
            def save(self):
                pass  # 模拟数据库保存
        print("正在生成测试用户......")
        dummy_seat = DummySeat()

        class DummyReservation:
            SeatID = dummy_seat
            Start = 9
            End = 12

        occupySeat(DummyReservation)
        print(f"占用后 Used: {dummy_seat.Used}")  # 应为 000000000111000000000000

        releaseSeat(DummyReservation)
        print(f"释放后 Used: {dummy_seat.Used}")  # 应恢复为 000000000000000000000000    




def main():
    test_demo=Demo()
    test_demo.test_getInformationOption()
    test_demo.test_startend2mask()
    test_demo.test_mask2startend()
    test_demo.test_human_read_accessable()
    test_demo.test_seatAvailable()
    test_demo.test_seat_management()
    test_demo.test_reservation_time()
    test_demo.test_human_readable_format()
    test_demo.test_sendemail()
    test_demo.test_inCampus()
    test_demo.test_get_deadline()
    test_demo.test_get_remind_time()
    test_demo.test_occupy_and_release_seat()

print("=> 开始测试 library app ..")
main()
