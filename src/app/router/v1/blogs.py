from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, crud
from app.core.deps import get_db

router = APIRouter()


@router.get("", response_model=List[schemas.BlogResponse])
def get_multi_blogs(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    """
    find all blogs.
    """
    blog = crud.blog.get_multi(db, skip=skip, limit=limit)

    if not blog:
        raise HTTPException(status_code=404, detail="blog not found")

    return blog


@router.get("/{id}", response_model=schemas.Blog)
def get_blog(id: int, db: Session = Depends(get_db)) -> Any:
    """
    find blog
    """
    blog = crud.blog.get(db, id=id)

    if not blog:
        raise HTTPException(status_code=404, detail="blog not found")

    return blog


@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.BlogResponse)
def create_blog(*, db: Session = Depends(get_db), payload: schemas.BlogCreate) -> Any:
    """
    Create new Blog.
    """
    blog = crud.blog.create(db, payload=payload)
    return blog


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.BlogResponse)
def update_blog(*, db: Session = Depends(get_db), id: int, blog_in: schemas.BlogUpdate) -> Any:
    """
    Update Blog.
    """
    blog = crud.blog.get(db, id=id)

    if not blog:
        raise HTTPException(status_code=404, detail="blog not found")

    if blog_in is None:
        raise HTTPException(status_code=400, detail="Bad Request Error")

    blog = crud.blog.update(db=db, db_obj=blog, obj_in=blog_in)

    return blog


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_blog(*, db: Session = Depends(get_db), id: int) -> Any:
    """
    Delete Blog.
    """
    blog = crud.blog.get(db, id=id)

    if not blog:
        raise HTTPException(status_code=404, detail="blog not found")

    return crud.blog.delete(db=db, db_obj=blog)


@router.post("/likes", status_code=status.HTTP_201_CREATED, response_model=schemas.BlogLikeResponse)
def create_blog_like(*, db: Session = Depends(get_db), paylod: schemas.BlogLikeCreate) -> Any:
    """
    Create new BlogLike. 중복 안되게 처리 필요
    """
    db_obj = crud.blog_like.create(db, payload=paylod)
    return db_obj


@router.delete("/{id}/likes/{like_id}", status_code=status.HTTP_200_OK)
def delete_blog_like(*, db: Session = Depends(get_db), id: int, like_id: int) -> Any:
    """
    Delete Blog.
    """
    blog_like = crud.blog_like.get(db, id=like_id, blog_id=id)

    if not blog_like:
        raise HTTPException(status_code=404, detail="blog_like not found")

    crud.blog_like.remove(db=db, db_obj=blog_like)

    return blog_like