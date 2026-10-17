# Asset provenance

## AI illustration

Built-in imagegen tool. Original hero file:
`/mnt/c/Users/noc/.codex/generated_images/01a111f0-b851-7940-ad82-042ddd2be9df/exec-563cf828-79bf-4cea-bb29-8b4556368912.png`

Hero assets: `dist/assets/hero-1600.webp`, `hero-800.webp`, `hero-480.webp`. Converted deterministically to responsive WebP. Displayed with an explicit illustration label; no claim that it depicts an actual restaurant dish or interior.

Final prompt:

> Use case: photorealistic-natural. Asset type: illustrative restaurant website hero photograph, landscape 3:2. Primary request: premium editorial Italian food still-life photograph for La Mela d’oro restaurant website. Scene/backdrop: dark rustic wood table with deep earthy olive tones, close food composition with no visible restaurant interior. Subject: one rustic margherita pizza with tomato sauce, mozzarella, and oregano as the exact toppings; partial plate of spaghetti with tomato sauce secondary at an edge. Pizza is the clear main focus. Style/medium: polished natural food photography, realistically appetizing, subtle film character. Composition/framing: landscape 3:2, close overhead/45-degree angle, pizza fills most of the frame, cropped secondary spaghetti at the perimeter; compelling crop that remains recognizable on mobile. Lighting/mood: soft natural daylight with gentle shadows and warm appetizing colors. Color palette: forest olive #25382c, antique gold #c7a45f accents, tomato reds and creamy mozzarella. Materials/textures: tactile charred crust, melted mozzarella, delicate oregano, worn dark wood, restrained linen accent. Constraints: exactly one image. Food illustration only, no claimed restaurant setting. No people, text, letters, logos, watermark. Do not add other toppings to the margherita; basil may appear only as a restrained table accent away from pizza.

## Supplied restaurant photographs

Seven distinct customer photos were supplied for this update. The eighth file (`1791350753176_...jpg`) is byte-identical to the dining-room photo and is intentionally omitted. The website uses resized, metadata-stripped WebP copies in `dist/assets/restaurant/`:

| Website asset | Supplied source photo | Placement |
| --- | --- | --- |
| `sushi-*` | `1791350744454_...jpg` | Menu discovery and gallery |
| `dining-room-*` | `1791350748565_...jpg` | Restaurant story and gallery |
| `guests-*` | `1791350757742_...jpg` | Ordering block and gallery |
| `set-table-750` | `1791350724832_...jpg` | Gallery |
| `birthday-table-1200` | `1791350730716_...jpg` | Gallery |
| `birthday-room-1200` | `1791350735181_...jpg` | Gallery |
| `archway-1200` | `1791350740875_...jpg` | Gallery |

The original supplied JPEGs remain in the user's attachment folder. The optimized files do not retain EXIF metadata. The AI pizza remains only in the hero and is labeled as an illustration; the former AI table scene was removed from the website.

## Supplied illustrations

- sushi.webp: illustration cropped from `5195c8a4388b7d40294c2c7280ae4789c2d93ee5.jpg` (page 7).
- pasta.webp: illustration cropped from `b55496ae74dcc6b2c43ddf8f4b02c584ffea051d.jpg` (page 16).
- original-menu/page-01.webp through page-25.webp: conversions of all 25 supplied files; mapping is in `../review/assets-inventory.json` and each menu item's source field.

Website does not fetch stock imagery or assets from L’Osteria.

## Fonts

Bebas Neue and Caveat, Google Fonts, SIL OFL. Self-hosted TTF files and licenses are shipped with the website. UI/body text uses system Arial/Helvetica. No requests to external font services are needed at runtime.

## Menu update · 15 October 2026

Customer clipboard photos are preserved in `source-menu/hot-drinks-2026-10-15.png` and `source-menu/japanese-cuisine-2026-10-15.png`. The hot-drinks photo supplies all 11 previously cropped prices and replaces `dist/assets/original-menu/page-23.webp`. The Japanese-cuisine photo confirms the existing items 190–192 and their prices (31.90 / 19.90 / 23.90 EUR); no duplicate items were added.

## Celebration videos · 17 October 2026

Four customer-supplied clips from the attachment folder were re-encoded in full to H.264/AAC MP4 with fast-start playback and stripped metadata. Native aspect ratios, duration, and audio are retained; no scenes were generated or combined. Files live in `dist/assets/celebrations/`. WebP posters were extracted at 8 seconds. Video files load only after a visitor selects a clip.

| Asset | Original filename | Duration |
| --- | --- | --- |
| `feier-1.mp4` | `AQM4Hq2dzLq9Ef2T6_vz7Wz27P_lEsUtGIQMr7Bx4D0oDLWcZQdRmE5_WmBCht5e4lZrBsp6rQ4S0gJKRUJ7o4Q3YFPbQMafeOJsCmnyhw.mp4` | 00:01:40.50 |
| `feier-2.mp4` | `AQMCKfbYCQnQy7OYpaUo40CSyX5173-lIB8eFEJBtpJ7IpzZg4Bwze_Dd7Sh_c80-wWKrRvnz42nAP_L7tEmtcu1FoiygTk-9kSztOn6ew.mp4` | 00:03:04.23 |
| `feier-3.mp4` | `AQOl-SsZFStLb85iTA45LRVp_ucURYsSDsKmbmtgjIye0WR6DbYKNhY4v2fLs2IAOXmvHdEu8Da1_q1NOe7YRWKa8jy0Ss1ysjmHeJyOpg.mp4` | 00:02:21.53 |
| `feier-4.mp4` | `AQPAYJaHy3V2UfKasxQ-1B7nUQ_SBDVmGVAgDYnz2t95FY-DeW6yTkn68qn3n2--ZB6lbubu31IKhjvZgGxwfnCzdvJA659BUvE9Yg9hng.mp4` | 00:01:03.00 |

The accompanying German copy about weekend birthdays, weddings, and family celebrations comes from the customer’s instruction on 17 October 2026. Party enquiries use the verified restaurant telephone number.
