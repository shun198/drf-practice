# given: テストの前提条件を設定
# テストを実行するために必要な状態やデータを準備するために使用

# and: 追加の前提条件を指定
# 複数の前提条件を連結するために使用

# when: テスト対象のアクションやイベントをトリガします
# テストしたい操作やイベントを実行するために使用されます
# たとえば、「ユーザーがログインボタンをクリックした場合」といった形で使用

# then: 期待される結果や振る舞いを指定
# テストが成功するために満たされるべき条件や確認すべき振る舞いを記述
Feature: ヘルスチェックAPI
    Background:
        Given APIClientを生成
        And ヘルスチェックAPIのURL

    Scenario Outline: 正常系のテスト
        Given ヘルスチェック成功時のJSONを設定
        When GET通信を実施
        Then レスポンスのステータスが200
        And 期待通りのJSONが返却されていること
