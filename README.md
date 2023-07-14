# kbo_ranking_visualize
requests+matplotlib+깃허브 액션 크보 순위 시각화 프로젝트

```
kbo_ranking_visualize
├─ .git
│  ├─ COMMIT_EDITMSG
│  ├─ config
│  ├─ description
│  ├─ FETCH_HEAD
│  ├─ HEAD
│  ├─ hooks
│  │  ├─ applypatch-msg.sample
│  │  ├─ commit-msg.sample
│  │  ├─ fsmonitor-watchman.sample
│  │  ├─ post-update.sample
│  │  ├─ pre-applypatch.sample
│  │  ├─ pre-commit.sample
│  │  ├─ pre-merge-commit.sample
│  │  ├─ pre-push.sample
│  │  ├─ pre-rebase.sample
│  │  ├─ pre-receive.sample
│  │  ├─ prepare-commit-msg.sample
│  │  └─ update.sample
│  ├─ index
│  ├─ info
│  │  └─ exclude
│  ├─ objects
│  │  ├─ 00
│  │  │  └─ 165dfb7abcb05a35d28533e44f38e5cea6c495
│  │  ├─ 03
│  │  │  ├─ 39cf28660050d22b5e0ed987d1c8ec9a11fc0b
│  │  │  └─ ae19c70e66352eecae694205c64448619fdf53
│  │  ├─ 06
│  │  │  └─ 471243693b26ea67af4cfa02687a3626891b04
│  │  ├─ 09
│  │  │  └─ bf08723adc0302c94400230bd5a6f022c64ea8
│  │  ├─ 0d
│  │  │  └─ a30ce0f4e79dda8b0e3c4311316e91525ac290
│  │  ├─ 19
│  │  │  ├─ 8029d7d60bae3d944781224d7b4fe9b99c7258
│  │  │  └─ c5ac7d78f3dbb03c71ed38e8a094d45253dc4e
│  │  ├─ 21
│  │  │  └─ 29d58c81d45cb9e72c5b8f54f047a745e1c2dd
│  │  ├─ 23
│  │  │  └─ 8961bf7a49fb150dec049850da0cbdc7d305ce
│  │  ├─ 24
│  │  │  └─ c099af86989b447f0187da558c59460fed5d90
│  │  ├─ 28
│  │  │  └─ b705ab3c885c36172b60224aa0a00b5f2e11cf
│  │  ├─ 30
│  │  │  └─ e49758467a873ec1384a48afcbfa83fee2dd97
│  │  ├─ 37
│  │  │  ├─ 55a4648123f7bbc2b841120f6e7702efa0ec83
│  │  │  └─ 9dd9807e52a26d67d56d3db41a550ae8e9491d
│  │  ├─ 3c
│  │  │  └─ a700d37bc5ff5b4613d7a643c229765e689a55
│  │  ├─ 40
│  │  │  └─ 5284feca63d09b312147989343352142427952
│  │  ├─ 42
│  │  │  └─ dab17831c8bac52f828deb0395290624d86252
│  │  ├─ 43
│  │  │  └─ f22b14618ff169dc81174f530d63ff4e87bbb4
│  │  ├─ 48
│  │  │  └─ a17b81fd9f3aef53be01efb9b60173778c6fc0
│  │  ├─ 49
│  │  │  └─ 9aed9f583852977525255f8af4d6e38c0aed69
│  │  ├─ 4c
│  │  │  └─ a1edfccc1b9378a909e433f775a86e7cd722e0
│  │  ├─ 4e
│  │  │  └─ 479cbcb55ea28776cdba0fb45658ff00d7af92
│  │  ├─ 55
│  │  │  └─ 10577a6a3505a59b14b1bb3660ac05bfc6aa82
│  │  ├─ 58
│  │  │  └─ 79abbccbed4b9af4b5ba0e01d97d2e86e7bb25
│  │  ├─ 69
│  │  │  └─ f0647f9fc94506b7c273abaffbace61da80555
│  │  ├─ 6a
│  │  │  └─ cbdc60c4394e520b000df8be1f724c4b1d8a73
│  │  ├─ 6b
│  │  │  └─ 6f67278a534fd503c6edb556061b254a469470
│  │  ├─ 6e
│  │  │  └─ bc35072b0f00272cd09dabdcae6748f3a55290
│  │  ├─ 6f
│  │  │  └─ f61a138e127be8fd7c8c7466a130ce4ca3d3ea
│  │  ├─ 71
│  │  │  └─ 2984a558ce909e5162ddba8c85033618244f5b
│  │  ├─ 79
│  │  │  └─ 7eff0350506b0eeaaf6143d8f47399106edcdd
│  │  ├─ 7a
│  │  │  └─ 7edb3debbe220614794428931a1c9a6fcf4f7f
│  │  ├─ 7d
│  │  │  └─ f3af5bc5308db55e6c7ba1b31aded05d95e5f9
│  │  ├─ 7f
│  │  │  └─ 90132af53752ec4d07d6ad9ca9c37ff8b82d28
│  │  ├─ 81
│  │  │  └─ e3f258257aa6e767c12eff66f47b267102a1b7
│  │  ├─ 82
│  │  │  └─ 1c7900db1912ddb6d0f55a30e38433e35e8aca
│  │  ├─ 86
│  │  │  ├─ 1b0c42f4e18a150345f2921087aeb4057de3e2
│  │  │  └─ 1e95b3e700d5a59ecac2eb13c9df1bc010f06a
│  │  ├─ 87
│  │  │  └─ 0c027a351a538f739876f537e4fe852d2aa796
│  │  ├─ 93
│  │  │  └─ 7a5b24dab739254520a3b664fdf44352e10dc3
│  │  ├─ 96
│  │  │  └─ baa625de2dd10b40fdc12826d48c1871ba299d
│  │  ├─ 97
│  │  │  └─ c87713b911d6d9d70881afc62cba8e1f2fb76a
│  │  ├─ 9b
│  │  │  └─ ef276e2c26d3d65747b9c777962f987e43f80c
│  │  ├─ 9e
│  │  │  ├─ 0f157a653ab096cc7209d0f693ce8b6bf520cf
│  │  │  └─ c6844fcf82b42eeaa8d1041cf6d3b6a1dc4dfa
│  │  ├─ a1
│  │  │  └─ 1f5b40c8a7f715f5013ad36b87ed330feeda85
│  │  ├─ a7
│  │  │  └─ 097093a8a1e68f448944dea443fd0d29c95ab7
│  │  ├─ a9
│  │  │  └─ 8cb65a6815d534f252e101bc81ce28546de088
│  │  ├─ ae
│  │  │  ├─ 34b3ddcd72d549e38adcbbffe9c5bd6387bbb6
│  │  │  └─ ca9742be61c3b391f49ceb512d23e1fad9d45d
│  │  ├─ b0
│  │  │  └─ 54a98b0604c3a74c2b5e3287d5f2d0d72e8ad9
│  │  ├─ b4
│  │  │  └─ e78f28adb3a362ad3391a300c3fd84ddff5e2f
│  │  ├─ b9
│  │  │  ├─ 53a0a507fb6fe1a336cf8e71f5ee86440571db
│  │  │  └─ d8bf9910936ea8b79d115e4f7314e20327d956
│  │  ├─ ba
│  │  │  └─ 1201416a0c5880583a9d8224d3328b8a08c53e
│  │  ├─ be
│  │  │  └─ 98550c6c12a3eb71d83374134f14746038b72e
│  │  ├─ bf
│  │  │  └─ c33c7d8e1bfd33394cdd95c89ebab100a36fba
│  │  ├─ c5
│  │  │  └─ 06c582a289f71d71dee2d98581516b5ab39394
│  │  ├─ ca
│  │  │  └─ 6fdad85b50b88ceda99e813b2e6f6ab1b77f37
│  │  ├─ d0
│  │  │  └─ 3216ff4d2ae4b1e8c42e57891ae614813108da
│  │  ├─ de
│  │  │  └─ 57d1a3193555b446d6e11d04e4fdd0b2b8cbf6
│  │  ├─ e0
│  │  │  └─ 90b3c6affb2fe64271e87e19bfc311ce7fa0b3
│  │  ├─ e8
│  │  │  └─ 5496840660bb3e63794927a4cd7317bfd52e4c
│  │  ├─ info
│  │  └─ pack
│  │     ├─ pack-2a0497d9c2a148f674bc19580eb4cb9821e952ac.idx
│  │     └─ pack-2a0497d9c2a148f674bc19580eb4cb9821e952ac.pack
│  ├─ ORIG_HEAD
│  ├─ packed-refs
│  └─ refs
│     ├─ heads
│     │  └─ main
│     ├─ remotes
│     │  └─ origin
│     │     ├─ HEAD
│     │     └─ main
│     └─ tags
├─ .gitignore
├─ app.py
├─ package-lock.json
├─ package.json
├─ README.md
├─ src
│  ├─ 404.html
│  ├─ index.html
│  └─ index.js
├─ static
│  ├─ 404.css
│  ├─ font.css
│  ├─ index.css
│  ├─ KakaoTalk_20230714_104223079_03.jpg
│  ├─ KBO2023-07-13.png
│  └─ KBO2023-07-14.png
└─ watermark.png

```