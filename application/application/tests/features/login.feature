Feature: ログインAPI
    Background:
        Given APIClientを生成
        And ログインAPIのURL

    Scenario Outline: 正常系テスト
        Given <permission>権限のユーザ
        And ログイン用のJSONを設定
        And  <permission>権限でログイン成功時のJSONを設定
        When POST通信を実施
        Then レスポンスのステータスが200
        And 期待通りのJSONが返却されていること

        Examples:
            | permission |
            | MANAGEMENT |
            | GENERAL |
            | PART_TIME |

    Scenario Outline: 社員番号またはパスワードが間違っている場合の異常系テスト
        Given 社員番号またはパスワードが間違っているJSONの設定
        And ログイン失敗時のJSONを設定
        When POST通信を実施
        Then レスポンスのステータスが400
        And 期待通りのJSONが返却されていること

        Examples:
            | permission |
            | MANAGEMENT |
            | GENERAL |
            | PART_TIME |
