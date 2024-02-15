from sqlalchemy.orm import Session
from schemas.blog import CreateBlog, UpdateBlog
from db.models.blog import Blog
from db.models.user import User


def create_new_blog(blog: CreateBlog, db: Session, author_id: int):
    print(author_id,"authorid")
    user_in_db = db.query(User).filter(User.id==author_id).first()
    print(user_in_db,"user in db")
    if not user_in_db:
        return
    blog=Blog(title=blog.title,
              slug=blog.slug,
              content = blog.content,
              author_id = author_id
              )
    db.add(blog)
    db.commit()
    db.refresh
    return blog

def get_blog_by_id(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog

def get_all_blogs(db: Session):
    blogs = db.query(Blog).filter(Blog.is_active==True).all()
    return blogs

def update_blog_by_id(id: int, blog:UpdateBlog ,db: Session,author_id: int =1):
    blog_in_db = db.query(Blog).filter(Blog.id == id).first()
    if not blog_in_db:
        return {"error":f"Blog with id {id} does not exist"}
    print(blog_in_db.author_id, " is the blog's authorid")
    print(author_id ," is current user's id")
    if not blog_in_db.author_id == author_id:
        return {"error":"only the author can modify the blog"}
    blog_in_db.title = blog.title
    blog_in_db.content = blog.content
    db.add(blog_in_db)
    db.commit()
    return blog_in_db

def delete_blog_by_id(id: int, db: Session, author_id: int =1):
    blog_in_db = db.query(Blog).filter(Blog.id==id)
    if not blog_in_db.first():
        return {"error":f"Blog with id {id} doesn't exist"}
    if not blog_in_db.first().author_id == author_id:
        return {"error":f"only the author can delete the blog"}
    blog_in_db.delete()
    db.commit()
    return {"msg":f"Blog with id {id} deleted"}

 