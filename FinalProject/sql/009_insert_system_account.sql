INSERT INTO
    IS601_S_Accounts (id, user_id, account)
VALUES (-1, null, 'snt_sys_acct') ON DUPLICATE KEY
UPDATE user_id = null;