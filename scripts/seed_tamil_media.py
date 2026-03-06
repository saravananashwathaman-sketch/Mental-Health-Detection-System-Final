import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import MediaContent
from datetime import datetime

def seed_tamil_media():
    app = create_app()
    with app.app_context():
        # Clear existing media if needed (optional)
        # MediaContent.query.delete()
        
        media_data = [
            # ── Silent / Introverted ──────────────────────────────────────────
            {
                "title": "Life of Ram",
                "type": "song",
                "personality_category": "Silent/Introverted",
                "source_url": "https://www.youtube.com/watch?v=6L2AnS50p_A",
                "description": "A soulful track from '96' celebrating solitude and peace.",
                "tags": "Peaceful, Solitude, Soulful",
                "thumbnail_url": "https://img.youtube.com/vi/6L2AnS50p_A/mqdefault.jpg",
                "language": "Tamil"
            },
            {
                "title": "New York Nagaram",
                "type": "song",
                "personality_category": "Silent/Introverted",
                "source_url": "https://www.youtube.com/watch?v=S0Tofv9XozQ",
                "description": "An AR Rahman classic from 'Sillunu Oru Kadhal' about long-distance yearning.",
                "tags": "Melody, Yearning, Serene",
                "thumbnail_url": "https://img.youtube.com/vi/S0Tofv9XozQ/mqdefault.jpg",
                "language": "Tamil"
            },
            {
                "title": "Nenjukkul Peidhidum",
                "type": "song",
                "personality_category": "Silent/Introverted",
                "source_url": "https://www.youtube.com/watch?v=FzLp_Kx8mMc",
                "description": "Beautiful acoustic melody from 'Vaaranam Aayiram'.",
                "tags": "Acoustic, Romantic, Calm",
                "thumbnail_url": "https://img.youtube.com/vi/FzLp_Kx8mMc/mqdefault.jpg",
                "language": "Tamil"
            },
            
            # ── Humor / Happy ─────────────────────────────────────────────────
            {
                "title": "Why This Kolaveri Di",
                "type": "song",
                "personality_category": "Humor",
                "source_url": "https://www.youtube.com/watch?v=YR12Z8f1UX8",
                "description": "The global viral hit from '3' with light-hearted humor.",
                "tags": "Viral, Funny, Catchy",
                "thumbnail_url": "https://img.youtube.com/vi/YR12Z8f1UX8/mqdefault.jpg",
                "language": "Tamil"
            },
            {
                "title": "Vaathi Coming",
                "type": "song",
                "personality_category": "Humor",
                "source_url": "https://www.youtube.com/watch?v=fRd_vYI4Oho",
                "description": "High-energy dance track from 'Master'.",
                "tags": "Dance, Energy, Fun",
                "thumbnail_url": "https://img.youtube.com/vi/fRd_vYI4Oho/mqdefault.jpg",
                "language": "Tamil"
            },
            {
                "title": "Rowdy Baby",
                "type": "song",
                "personality_category": "Humor",
                "source_url": "https://www.youtube.com/watch?v=x6Q7c9AyDz0",
                "description": "Peppy dance number from 'Maari 2'.",
                "tags": "Dance, Peppy, Fun",
                "thumbnail_url": "https://img.youtube.com/vi/x6Q7c9AyDz0/mqdefault.jpg",
                "language": "Tamil"
            },
            
            # ── Motivated ─────────────────────────────────────────────────────
            {
                "title": "Singappenney",
                "type": "song",
                "personality_category": "Motivated",
                "source_url": "https://www.youtube.com/watch?v=68D0YjS5R-Y",
                "description": "Inspiring anthem for women's strength from 'Bigil'.",
                "tags": "Inspirational, Power, Anthem",
                "thumbnail_url": "https://img.youtube.com/vi/68D0YjS5R-Y/mqdefault.jpg",
                "language": "Tamil"
            },
            {
                "title": "Aalaporan Tamizhan",
                "type": "song",
                "personality_category": "Motivated",
                "source_url": "https://www.youtube.com/watch?v=33_O_vS62S8",
                "description": "Energetic track celebrating Tamil culture and pride from 'Mersal'.",
                "tags": "Pride, Energy, Anthem",
                "thumbnail_url": "https://img.youtube.com/vi/33_O_vS62S8/mqdefault.jpg",
                "language": "Tamil"
            },
            {
                "title": "Ethir Neechal Title Song",
                "type": "song",
                "personality_category": "Motivated",
                "source_url": "https://www.youtube.com/watch?v=Kz6oasT76_o",
                "description": "Motivational track about struggling and winning.",
                "tags": "Success, Grind, Power",
                "thumbnail_url": "https://img.youtube.com/vi/Kz6oasT76_o/mqdefault.jpg",
                "language": "Tamil"
            },
            
            # ── Nostalgic ─────────────────────────────────────────────────────
            {
                "title": "Munbe Vaa",
                "type": "song",
                "personality_category": "Nostalgic",
                "source_url": "https://www.youtube.com/watch?v=3S_0_vO_vV8",
                "description": "Timeless melody about love and longing from 'Sillunu Oru Kadhal'.",
                "tags": "Melody, Retro, Romantic",
                "thumbnail_url": "https://img.youtube.com/vi/3S_0_vO_vV8/mqdefault.jpg",
                "language": "Tamil"
            },
            {
                "title": "Pachai Nirame",
                "type": "song",
                "personality_category": "Nostalgic",
                "source_url": "https://www.youtube.com/watch?v=Qit-e-1N_N8",
                "description": "Vibrant and nostalgic track from Mani Ratnam's 'Alaipayuthey'.",
                "tags": "Colors, Retro, AR Rahman",
                "thumbnail_url": "https://img.youtube.com/vi/Qit-e-1N_N8/mqdefault.jpg",
                "language": "Tamil"
            },
            {
                "title": "Uyire Uyire",
                "type": "song",
                "personality_category": "Nostalgic",
                "source_url": "https://www.youtube.com/watch?v=3Y8v-9W-Y7g",
                "description": "Soul-stirring classic from 'Bombay'.",
                "tags": "Retro, Emotion, Classic",
                "thumbnail_url": "https://img.youtube.com/vi/3Y8v-9W-Y7g/mqdefault.jpg",
                "language": "Tamil"
            },
            
            # ── Trends ────────────────────────────────────────────────────────
            {
                "title": "Bloody Sweet",
                "type": "song",
                "personality_category": "Trends",
                "source_url": "https://www.youtube.com/watch?v=9_f_uV_p_7Q",
                "description": "Trending title track from 'Leo'.",
                "tags": "Trending, Action, Style",
                "thumbnail_url": "https://img.youtube.com/vi/9_f_uV_p_7Q/mqdefault.jpg",
                "language": "Tamil"
            },
            {
                "title": "Kaavaalaa",
                "type": "song",
                "personality_category": "Trends",
                "source_url": "https://www.youtube.com/watch?v=lX44CAz-JhU",
                "description": "Recent viral dance track from 'Jailer'.",
                "tags": "Viral, Dance, Recent",
                "thumbnail_url": "https://img.youtube.com/vi/lX44CAz-JhU/mqdefault.jpg",
                "language": "Tamil"
            }
        ]

        for item in media_data:
            exists = MediaContent.query.filter_by(title=item["title"]).first()
            if not exists:
                content = MediaContent(
                    title=item["title"],
                    type=item["type"],
                    personality_category=item["personality_category"],
                    source_url=item["source_url"],
                    description=item["description"],
                    tags=item["tags"],
                    thumbnail_url=item["thumbnail_url"],
                    language=item["language"]
                )
                db.session.add(content)
        
        db.session.commit()
        print("Tamil media content seeded successfully!")

if __name__ == "__main__":
    seed_tamil_media()
