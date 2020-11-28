from ypb_website.moderation_staff import ModerationStaff


# Requirement 3.5.2.2
def test_approve_pending_transactions():
    moderation_staff = ModerationStaff('adminzhengs46', 'Sean', 'Watson', 'Moderation', ["""list of customers"""],
                                       ["""list of pending transactions"""])
    assert moderation_staff.approve_transaction('someusername',
                                                12312) == True, 'the pending transaction should be approved.'
