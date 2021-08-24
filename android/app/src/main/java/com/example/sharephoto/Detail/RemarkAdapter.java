package com.example.sharephoto.Detail;


import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.example.sharephoto.R;

import java.util.List;

import de.hdodenhof.circleimageview.CircleImageView;

public class RemarkAdapter extends RecyclerView.Adapter<RemarkAdapter.ViewHolder> {

    private Context context;
    private List<Remark> remarks;
    private int resourceId;

    public RemarkAdapter(Context context, List<Remark> remarks, int resourceId) {
        this.context = context;
        this.remarks = remarks;
        this.resourceId = resourceId;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(context).inflate(resourceId, parent, false);
        ViewHolder holder = new ViewHolder(view);
        return holder;
    }

    @Override
    public void onBindViewHolder(@NonNull RemarkAdapter.ViewHolder holder, int position) {
        Remark remark = remarks.get(position);
        holder.remark_icon.setImageResource(remark.getIcon());
        holder.remark_username.setText(remark.getUsername());
        holder.remark_content.setText(remark.getContent());
        holder.remark_date.setText(remark.getDate());
        holder.remark_status.setSelected(remark.isStatus());
        holder.remark_status.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                holder.remark_status.setSelected(!holder.remark_status.isSelected());
            }
        });
    }


    @Override
    public int getItemCount() {
        return remarks.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder {
        CircleImageView remark_icon;
        TextView remark_username;
        TextView remark_date;
        ImageView remark_status;
        TextView remark_content;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            remark_icon = itemView.findViewById(R.id.remark_icon);
            remark_username = itemView.findViewById(R.id.remark_username);
            remark_date = itemView.findViewById(R.id.remark_date);
            remark_status = itemView.findViewById(R.id.remark_status);
            remark_content = itemView.findViewById(R.id.remark_content);
        }
    }
}
